#code by pranay
#date 23-09-26

#defining the required  function, that checks the stable signal and returns the inddex
def firstStable(a, n, tolerance):
    for i in range(n - 1):
        #checking if the difference is less than the rolerable number
        if abs(a[i + 1] - a[i]) <= tolerance:
            return i
        #return the negative stability as -1
    return -1


#reading the number string
n = int(input())
#converting number string into array
a = list(map(float, input().split()))
tolerance = float(input())

print(firstStable(a, n, tolerance))
