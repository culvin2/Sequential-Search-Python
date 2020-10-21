testlist=[1,2,32,44,88,13,0]
a = 1
b = 32
def SequentialSearh(testlist,a):
    for i in range(0,len(testlist)-1,1) :
        if testlist[i]== a :
            print("Found in index : ")
            return i
            break
    else:
         print("Sorry, not found!")
         return False

print(SequentialSearh(testlist,a))
print(SequentialSearh(testlist,b))

