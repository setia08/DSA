arr = [34, 20, 10]

if len(arr)<1:
    print(-1)
    exit()

arr.sort()
biggest=arr[-1]
while biggest in arr:
    arr.remove(biggest)

if len(arr) < 1:
    print(-1)
    exit()

print(arr[-1])