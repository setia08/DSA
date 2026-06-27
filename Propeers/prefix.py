arr=[1,2,3,4]
prefix=[arr[0]]*len(arr)
print(prefix)


for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print("Output",arr)
print(prefix)

# if we want sum of range(1,3) then we can do is

print(prefix[3]-prefix[0])