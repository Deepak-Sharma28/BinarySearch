arr = [12,16,65,70,80]


low = 0

high = len(arr)-1

element = int(input())
def binarysearch(arr,low,high,element):
    if low<high :
        mid = (low+high)//2
        if element<arr[mid]:
            return binarysearch(arr,low,mid-1,element)
        elif element>arr[mid]:
            return binarysearch(arr,mid+1,high,element)
        else:
            return mid
    else:
        return -1       

result = binarysearch(arr,low,high,element)
if result != -1 :
    print("position of the element is "+str(result))
else:
    print("element has not found")