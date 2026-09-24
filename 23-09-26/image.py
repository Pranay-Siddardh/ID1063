#code by pranay
#date 23-09-26

from PIL import Image

#Gray_scale converter
img = Image.open("image.jpg").convert("L")

threshold = int(input("Enter threshold (0-255): "))

width, height = img.size

#creating the image object
bw = Image.new("L", (width, height))

with open("grayscale.txt", "w") as gray_file,  
     open("black_white.txt", "w") as bw_file:

    for y in range(height):
        gray_row = []
        bw_row = []

        for x in range(width):
            gray = img.getpixel((x, y))

           gray_row.append(str(gray))

            #Black and white algorithm
            if gray >= threshold:
                value = 255
            else:
                value = 0

            bw_row.append(str(value))
            bw.putpixel((x, y), value)

        gray_file.write(" ".join(gray_row) + "\n")
        bw_file.write(" ".join(bw_row) + "\n")

img.save("grayscale.png")
bw.save("black_white.png")
