def max_perimeter(arr):
    max_p = 0
    # abhi mere pass array h 6,1,6,5,8,4
    # ab isme se mujhe select krne h teen but 
    # teeno same nhi hone chahiye
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                a, b, c = arr[i], arr[j], arr[k]

                if a + b > c and a + c > b and b + c > a:
                    perimeter = a + b + c

                    if perimeter > max_p:
                        max_p = perimeter

    return max_p



def main():
    print(max_perimeter([6,1,6,5,8,4]))

main()