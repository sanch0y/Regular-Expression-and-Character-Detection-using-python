#Lists for check
key_words = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally', 'float', 'for', 'if', 'implements', 'import', 'instanceof', 'int', 'interface', 'long', 'native', 'new', 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'void', 'while']
math_op = ['+', '-', '*', '/', '%', '=']
logical_op = ['!', '>', '<', '&&', '||']

#Blank lists to insert values and final print
k_w = []
identifiers = []
m_o = []
l_o = []
numeric_val = []
others = []

# Open a file
fo = open("input.txt", "r+")

while True :
        line = fo.read()
        if not line :
                break
        else :
                fetch = line.split()
for i in fetch :
        token = i
        #print(token)
        for j in token :#**Others
                if(j == ',' or j == ';' or j == '(' or j == '{' or j == '[' or j == ')' or j == '}' or j == ']') :
                        others.append(j)#Others**
        for j in key_words :
                if(i == j) :
                        k_w.append(i)
        for j in math_op:
                if (i == j):
                        m_o.append(i)
        for j in logical_op:
                if (i == j):
                        l_o.append(i)
        for j in token:#**Neumeric values
                if (j == ';'):
                        temp = i.split()
                        for k in temp:
                                insideTemp = k.split(";")
                        for l in insideTemp:
                                if(l.replace('.','',1).isdigit() or l.isdigit()):
                                        numeric_val.append(l)#Neumeric values**
        for j in token:#**Identifiers
                if (j == ',' or j == ';'):
                        temp2 = i.split()
                        for k in temp2:
                                insideTemp2 = k.split(",")
                                insideTemp3 = k.split(";")
                                for l in insideTemp2:
                                        if (len(insideTemp2) == 2 and l.isalpha()):
                                                identifiers.append(l)
                                for m in insideTemp3:
                                        if (len(insideTemp3) == 2 and m.isalpha()):
                                                identifiers.append(m)#Identifiers**
                                                # print(" *temp2* ", temp2)
                                                # print(" *insideTemp2* ", insideTemp2)
                                                # print(" *insideTemp3* ", insideTemp3)
#Printing Before
print("Key Words : ", list(set(k_w)))
print("Identifiers : ", list(set(identifiers)))
print("Math Operators : ", list(set(m_o)))
print("Logical Operators : ", list(set(l_o)))
print("Numerical Values : ", list(set(numeric_val)))
print("Others : ", list(set(others)))

# Close opened file
fo.close()