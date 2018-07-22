#Zero Or More
characters_1 = []



#Zero Or More
def Zero_Or_More(inpLst):
    c = 0
    dot = 0
    invalid = False
    for i in inpLst:
        inputSplit = i
        for j in inputSplit:
            print(j)
            if (j.isdigit()):
                c = 0
            if (j.isidentifier()):
                invalid = True
                break
            if (j == '.' and dot == 0):
                dot+=1
            elif(j == '.' and dot != 0):
                invalid = True
                break
                characters_1.append(j)


    if(invalid == True or c == 1):
        print("Reject")
    elif(c == 0):
        print("Accept")


    print(characters_1)


#Taking input
inputList = []
countM = int(input('Give m: '))
c2 = 0
while (c2 < countM):
    i = input()
    inputList.append(i)
    Zero_Or_More(inputList)
    c2 = c2 + 1

#Sending input inside functions
#1
#Zero_Or_More(inputList)