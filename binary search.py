def binarysearch(list,low, high, value):
    if(low <= high):
        mid = (low + (high - low))//2
        if(list[mid]==value):
            print("Found at position " +str(mid+1))
            return mid
        elif(list[mid]<value):
            return binarysearch(list,mid+1,high,value)
        else:
            return binarysearch(list,low,mid-1,value)
    else:
        print("not found")
        return -1

list = [ 2, 3, 4, 10, 40 ]
value = 40
binarysearch(list,0,len(list)-1,value)
