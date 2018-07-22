#Zero Or More
characters_1 = []
#One or More
characters_2 = []
#Once Or Not At All
characters_3 = []
#Character Classes
characters_4 = []
#Negation
characters_5 = []
#Exactly_N_Times
characters_6 = []

#Zero Or More
#a(bc)*de
def Zero_Or_More(inpLst):
    for i in inpLst:
        inputSplit = i
        for j in inputSplit:
            if (j.isidentifier()):
                characters_1.append(j)

    c = 0
    for index,k in enumerate(characters_1):
        if(k == 'b'):
            c+=1
            if(characters_1[index+1] == 'c'):
                c+=1

    if( len(characters_1) >= 3 ):
        if(characters_1[0] == 'a' and characters_1[-2] == 'd' and characters_1[-1] == 'e'):
            if(c%2 == 0):
                print("1 : ","Valid")
            else:
                print("1 : ","Invalid")
        else:
            print("1 : ","Invalid")
    else:
        print("1 : ","Invalid")

    print("1 : ",characters_1)



#One or More
#a(bc)+de
def One_Or_More(inpLst):
    for i in inpLst:
        inputSplit = i
        for j in inputSplit:
            if (j.isidentifier()):
                characters_2.append(j)

    c = 0
    for index, k in enumerate(characters_2):
        if (k == 'b'):
            c += 1
            if (characters_2[index + 1] == 'c'):
                c += 1

    if( len(characters_2) >= 5 ):
        if (characters_2[0] == 'a' and characters_2[-2] == 'd' and characters_2[-1] == 'e' and c!=0):
            if (c % 2 == 0):
                print("2 : ","Valid")
            else:
                print("2 : ","Invalid")
        else:
            print("2 : ","Invalid")
    else:
        print("2 : ","Invalid")

    print("2 : ",characters_2)



#Once Or Not At All
#a(bc)?de
def Once_Or_Not_At_All(inpLst):
    for i in inpLst:
        inputSplit = i
        for j in inputSplit:
            if (j.isidentifier()):
                characters_3.append(j)

    c = 0
    for index, k in enumerate(characters_3):
        if (k == 'b'):
            c += 1
            if (characters_3[index + 1] == 'c'):
                c += 1

    if ( len(characters_3) >= 3 ):
        if (characters_3[0] == 'a' and characters_3[-2] == 'd' and characters_3[-1] == 'e'):
            if (c == 0 or c == 2):
                print("3 : ", "Valid")
            else:
                print("3 : ", "Invalid")
        else:
            print("3 : ", "Invalid")
    else:
        print("3 : ", "Invalid")

    print("3 : ",characters_3)



#Character Classes
#[a-m]*
def Character_Classes(inpLst):
    for i in inpLst:
        inputSplit = i
        for j in inputSplit:
            if (j.isidentifier()):
                characters_4.append(j)

    c = 0
    for k in characters_4:
        chaR = k
        if(ord(k) >= 97 and ord(k) <= 109):
            c+=1

    if (c == len(characters_4)):
        print("4 : ", "Valid")
    else:
        print("4 : ", "Invalid")
    print("4 : ", characters_4)



#Negation
#[^aeiou]
def Negation(inpLst):
    for i in inpLst:
        inputSplit = i
        for j in inputSplit:
            if (j.isidentifier()):
                characters_5.append(j)
    c = 0
    for k in characters_5:
        if(k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u'):
            c = 1
            break

    if(c == 1):
        print("5 : ", "Invalid")
    else:
        print("5 : ", "Valid")

    print("5 : ", characters_5)



#Exactly N Times
#[^aeiou]{6}
def Exactly_N_Times(inpLst):
    for i in inpLst:
        inputSplit = i
        for j in inputSplit:
            if (j.isidentifier()):
                characters_6.append(j)
    c = 0
    c1 = 0
    c2 = 0
    for k in characters_6:
        if(c < 6):
            c+=1
            if (k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u'):
                c1 = 1
                break
            else:
                c1 = 0
        else:
            c2 = 1
            break

    if(c1 == 1):
        print("6 : ", "Invalid")
    elif(c2 == 1):
        print("6 : ", "Invalid")
    else:
        print("6 : ", "Valid")

    print("6 : ", characters_6)




#Taking input
inputList = []
countM = int(input('Give m: '))
c2 = 0
while (c2 < countM):
    i = input()
    inputList.append(i)
    c2 = c2 + 1

#Sending input inside functions
#1
Zero_Or_More(inputList)
#2
One_Or_More(inputList)
#3
Once_Or_Not_At_All(inputList)
#4
Character_Classes(inputList)
#5
Negation(inputList)
#6
Exactly_N_Times(inputList)