#Reverse an Array in groups

arr= [1,2,3,4,5,6,7,8]
k=3
result=[]
for i in range(0,len(arr),k):
    result.extend(arr[i:i+k][::-1])

print(result)