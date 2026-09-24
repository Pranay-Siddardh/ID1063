import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# STEP 1: READ THE JPG AND EXTRACT THE RAW RGB MATRIX
# ==============================================================================
def load_jpg_as_rgb(image_path):
    """
    Reads a JPEG image file from disk and loads it as a 3D NumPy array.
    Shape: (Height, Width, 3) where channels are [Red, Green, Blue].
    """
    try:
        import imageio.v3 as iio
        rgb_matrix = iio.imread(image_path)
    except ImportError:
        rgb_matrix = plt.imread(image_path)
        
    return rgb_matrix.astype(np.float32)


# ==============================================================================
# STEP 2: CONVERT RAW RGB MATRIX TO DECOUPLED YCbCr MATRIX
# ==============================================================================
def rgb_to_ycbcr(rgb_matrix):
    """
    Converts raw RGB pixel tuples into YCbCr space using ITU-R BT.601 formulas.
      - Y: Isolates Brightness (Luminance)
      - Cb & Cr: Isolate Color (Chrominance) offsets
    """
    R = rgb_matrix[:, :, 0]
    G = rgb_matrix[:, :, 1]
    B = rgb_matrix[:, :, 2]

    # Calculate Luminance (Y) and Chrominance (Cb, Cr)
    Y  = 0.299 * R + 0.587 * G + 0.114 * B
    Cb = 128 - 0.168736 * R - 0.331264 * G + 0.5 * B
    Cr = 128 + 0.5 * R - 0.418688 * G - 0.081312 * B

    return np.dstack((Y, Cb, Cr))


# ==============================================================================
# STEP 3: CONVERT TO GRAYSCALE (DISCARD COLOR CHANNELS)
# ==============================================================================
def ycbcr_to_grayscale(ycbcr_matrix):
    """
    Drops Cb and Cr channels completely, returning a 2D scalar array of Y values.
    Transforms memory structure from (Height, Width, 3) -> (Height, Width).
    """
    grayscale_matrix = ycbcr_matrix[:, :, 0]
    return np.clip(grayscale_matrix, 0, 255).astype(np.uint8)


# ==============================================================================
# STEP 4A: STATIC 128 REFERENCE THRESHOLDING (THE "REFERENCE BREAKER")
# ==============================================================================
def grayscale_to_static_bw(grayscale_matrix, threshold=128):
    """
    Applies a fixed, static threshold at 128 (midpoint of [0, 255]).
    
    Why is this a "reference breaker"?
      - If an image is overexposed (too bright) or underexposed (too dark),
        this naive method breaks down, losing fine details completely!
    """
    # Hardcoded threshold at 128
    bw_static = np.where(grayscale_matrix >= threshold, 255, 0).astype(np.uint8)
    return bw_static


# ==============================================================================
# STEP 4B: ADAPTIVE DYNAMICALLY SCALED BLACK & WHITE ALGORITHM
# ==============================================================================
def grayscale_to_adaptive_bw(grayscale_matrix):
    """
    Calculates the MEAN INTENSITY (mu) of the image and thresholds dynamically.
    Guarantees adaptive contrast scaling regardless of lighting!
    """
    mu = np.mean(grayscale_matrix)
    print(f"[INFO] Image Dynamic Threshold Mean (μ): {mu:.2f}")

    bw_adaptive = np.where(grayscale_matrix >= mu, 255, 0).astype(np.uint8)
    return bw_adaptive


# ==============================================================================
# EXECUTION PIPELINE
# ==============================================================================
if __name__ == "__main__":
    image_path = "input.jpg"

    print("Executing Image Processing Pipeline...")
    
    # 1. Pipeline Execution
    raw_rgb      = load_jpg_as_rgb(image_path)
    ycbcr        = rgb_to_ycbcr(raw_rgb)
    grayscale    = ycbcr_to_grayscale(ycbcr)
    
    # 2. Thresholding Algorithms
    static_bw    = grayscale_to_static_bw(grayscale, threshold=128)
    adaptive_bw  = grayscale_to_adaptive_bw(grayscale)

    # 3. Print Matrix Verifications
    print("\n==================================================")
    print("      MATRIX DATA STRUCTURE VERIFICATION")
    print("==================================================")
    print(f"1. Raw RGB Matrix Shape       : {raw_rgb.shape} (H, W, [R,G,B] Tuples)")
    print(f"2. YCbCr Matrix Shape         : {ycbcr.shape} (H, W, [Y,Cb,Cr] Tuples)")
    print(f"3. Grayscale Array Shape      : {grayscale.shape} (H, W) 2D Scalar Array")
    print(f"4. Static B&W Shape (128 Ref) : {static_bw.shape} (H, W) 2D Binary Array")
    print(f"5. Adaptive B&W Array Shape   : {adaptive_bw.shape} (H, W) 2D Binary Array")
    print("==================================================\n")

    # 4. Save Outputs
    plt.imsave("output_grayscale.png", grayscale, cmap='gray')
    plt.imsave("output_ref.png", static_bw, cmap='gray')            # Static 128 reference
    plt.imsave("output_adaptive_bw.png", adaptive_bw, cmap='gray')  # Dynamic adaptive output
    
    print("[SUCCESS] Files successfully saved:")
    print("  - output_grayscale.png")
    print("  - output_ref.png (Static 128 Reference Breaker)")
    print("  - output_adaptive_bw.png (Adaptive Dynamic Threshold)")
