arr = [8, 2, 4, 5, 3, 7, 1]

# OOutput should be 6
n = len(arr)
arr.sort()
small=min(arr)
largest=max(arr)

for i in range(small, largest+1):
    if i not in arr:
        print(i)
        break
else:
    print("All Included")


#other way i can think of is 

for i in range(len(arr)-1):
    if arr[i]+1 !=arr[i+1]:
        print(arr[i] + 1)
        break