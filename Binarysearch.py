def binarysearch(arr,k):
    low,high=0,len(arr)
    while low<high:
        mid=(low+high) // 2
        if k<arr[mid]:
            high=mid
        elif k>arr[mid]:
            low=mid+1
        else:
            return mid
    return-1
arr=[]
element=int(input("Enter the no of element"))
for i in range(element):
    ele=int(input("Enter the element"))
    arr.append(ele)
print(arr)
k=int(input("Enter the element to be searched"))
result=binarysearch(arr,k)
if result !=-1:
    print("search successful")
else:
    print("search Unsuccessful")