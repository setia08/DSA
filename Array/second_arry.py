arr = [10, 5, 10]

if len(arr)<1:
    print(-1)
    exit()

biggest=arr[0]

for i in arr:
    if i>biggest:
        biggest=i

while biggest in arr:
    arr.remove(biggest)

second=arr[0] 

for i in arr:
    if i>=second:
        second=i

if second==biggest:
    print(-1)
    exit()

print(second)
