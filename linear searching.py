def linearsearch(list,value):
    for i in range(len(list)):
        if(list[i]==value):
             print("Found at position "+ str(i+1))
             return True
    print("Not found")
    return True


list = [ 2, 3, 4, 10, 40 ]
value = 11
linearsearch(list,value)