# Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
# Output: {3, 4, 5, 6, 1, 2}
def rotate(arr,d):
    n=len(arr)
    res=[0]*n
    for i in range(len(arr)):
        res[i]=arr[(i+d)%n] 
    return res



def main():
    arr=[1, 2, 3, 4, 5, 6]
    d=2
    print(rotate(arr, d))

main()