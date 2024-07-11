#!/usr/bin/env python
# coding: utf-8

# In[68]:


dict_1 = { 'add':'10000',  'sub':'10001',  'mov imm':'10010', 'mov reg':'10011', 'ld':'10100',
           'st':'10101', 'mul':'10110', 'div':'10111', 'rs':'11000', 'ls':'11001',
           'xor':'11010', 'or':'11011', 'and':'11100',  'not':'11101',
           'cmp':'11110',  'jmp':'11111',  'jlt':'01100', 'jgt':'01101',
           'je':'01111', 'hlt':'01010'
          }
dict_2 = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110', 'FLAGS': '111'}

operations = ['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']

Type_A = ['add', 'sub', 'mul', 'xor', 'or', 'and']
Type_B = ['mov', 'rs', 'ls']
Type_C = ['mov', 'div', 'not', 'cmp']
Type_D = ['ld', 'st']
Type_E = ['jmp', 'jlt', 'jgt', 'je']
Type_F = ['hlt']

file1 = "INPUT.txt"
file2 = "OUTPUT.txt"
f2 = open(file2,"w")
f2.close()

f = open(file1,"r")   #open input file 
s = f.read()          #read file as string 
f.close()
l = s.split(",")      #list of strings (seperated by commas)

for i in l:
    l2 = i.split("\n")
Lst = l2                # each element of the list is the line of one ISA 
#print(Lst), print("\n") # DELETE
L = []
for i in Lst:
    l = i.split()
    L.append(l)

#print("L : ",L)               #2D array with                                            #DELETE
                                    

OP = []                  # opreation order , teking line 
for i in L:
    if i == []:
        pass
    else:
        OP.append(i[0])
    
#print("OP: ",OP)                 #D

Snd = []    # stores the 2nd element of instructio of each line
for i in L:
    try:
        Snd.append(i[1])
    except IndexError:
        pass

#print("Snd: ",Snd)   
def binary(n):
    var = format(n, '08b')     # minimun 8 bit representation
    return var
def m_add(x):              # memory address of the variable 
    s = "var"
    count = 0
    for i in OP:
        if i == s:
            pass
        else:
            count = count + 1
    indx = 0
    for i in range(len(Snd)):
        if Snd[i] == x:
            indx = indx + i
    z = count + indx 
    n = binary(z)
    str_ = str(n)
    return str_
    
def RESULT(L,OP):
    for i in L:
        if i == []:
            continue
        elif i[0] in Type_A:
            el = dict_1[i[0]] + '00'+ dict_2[i[1]] +dict_2[i[2]]+ dict_2[i[3]]
            #print(el)
            e = el 
            f2 = open(file2,"a")
            f2.write(e)
            f2.write("\n")
            f2.close()
        elif i[0] in Type_B and i[2][0] == '$':
            s = i[2][1:]
            n = int(s)
            bn = binary(n)
            string = str(bn)
            if i[0] == 'mov':      #this mov is for immediate value
                el = dict_1['mov imm'] + dict_2[i[1]] + string
                #print(el)
                e = el 
                f2 = open(file2,"a")
                f2.write(e)
                f2.write("\n")
                f2.close()
            else:
                el = dict_1[i[0]] + dict_2[i[1]] + string
                #print(el)
                e = el 
                f2 = open(file2,"a")
                f2.write(e)
                f2.write("\n")
                f2.close()
                
        elif i[0] in Type_C:
            if i[0] == 'mov':
                el = dict_1[i[0]] + "00000" + dict_2[i[1]] + dict_2[i[2]]
                #print(el)
                e = el
                f2 = open(file2,"a")
                f2.write(e)
                f2.writ2("\n")
                f2.close()
            else:
                el = dict_1[i[0]] + "00000" + dict_2[i[1]] + dict_2[i[2]]
                #print(el)
                e = el 
                f2 = open(file2,"a")
                f2.write(e)
                f2.write("\n")
                f2.close()
            
        elif i[0] in Type_D:
            x = i[2]
            s = m_add(x)
            el = dict_1[i[0]] + dict_2[i[1]] + s
            #print(el)                                # DELETE
            e =  el 
            f2 = open(file2,"a")
            f2.write(e)
            f2.write("\n")
            f2.close()
            
        elif i[0] in Type_E:
            x = i[1]
            s = m_add(x)
            el = dict_1[i[0]] +"000" + s
            #print(el)                             # DELETE
            f2 = open(file2, "a")
            f2.write(el)
            f2.write("\n")
            f2.close()
            
        elif i[0] in Type_F:
            el = dict_1[i[0]] + "00000000000"
            #print(el)                            # DELETE
            e = el
            f2 = open(file2,"a")
            f2.write(e)
            f2.write("\n")
            f2.close()
        

#RESULT(L,OP)                #delete
def e_hlt(L,OP):       # CHECK the correct position of the "hlt" instruction
    E = 0
    if 'hlt' not in OP:
        E = 1
        msg = "Syntax Error:  Missing hlt instruction"
        f2 = open(file2, "a")
        f2.write(msg)
        f2.close()
        return E
    else:
        if ('hlt' in OP) and (OP[-1] != 'hlt'):
            E = 1
            count = 0
            for i in L:
                if i == []:
                    count = count + 1
                    continue
                if i[0] == 'hlt':
                    count = count + 1
                    break
                count = count + 1
            v = str(count)
            msg = "Syntax Error: 'hlt' not used as the last instruction ---> line: " + v
            f2 = open(file2,"a")
            f2.write(msg)
            f2.close()
            return E
    return E
def e_imm(L, OP):    # check the error in imm values
    E = 0
    c = 0            # counts the line no 
    for i in L:
        if i == []:
            pass
        elif i[0] in Type_B and i[2][0] == '$':
            
            s = i[2][1:]
            n = int(s)
            if (type(n) != int) or (n<0 or n>255):
                c = c + 1
                E = 1
                msg = "Error: Invalid Imm value ---> line no " + str(c)
                f2 = open(file2,"a")
                f2.write(msg)
                f2.close()
                return E
            
        c = c + 1
    return E
def e_mem_add(L,OP):      #Checks error in memory address
    E = 0
    c = 0
    cn = 0
    for i in L:             # >8bit error detector
        if i == []:
            c = c + 1
            continue                  #  PLESE VISIT AGAIN
            
        if i[0] in Type_D:
            x = i[2]
            s = m_add(x)
            if len(s)>8:
                E = 1
                c = c + 1
                msg = "Error: Memory address is more than 8 bit --->line: " + str(c)
                f2 = open(file2,"a")
                f2.write(msg)
                f2.close()
                return E
            else:
                pass
        if i[0] in Type_E:
            x = i[1]
            s = m_add(x)
            if len(s)>8:
                E = 1
                c = c + 1
                msg = "Error: Memory address is more than 8 bit --->line: " + str(c)
                f2 = open(file2,"a")
                f2.write(msg)
                f2.close()
                return E
            else:
                pass
        c = c + 1
    for i in L:        # check if memory add_ is not from registors
        if i == []:
            cn = cn + 1
            continue
               
        if i[0] in Type_D:
            x = i[2]
            key_list = list(dict_2.keys())
            if x in key_list:
                cn = cn + 1
                E = 1
                msg = "Syntax Error: memory address must be a variable --->line: " + str(cn)
                f2 = open(file2,"a")
                f2.write(msg)
                f2.close()
                return E
            else:
                pass
        if i[0] in Type_E:
            x = i[1]
            key_list = list(dict_2.keys())
            if x in key_list:
                cn = cn + 1
                E = 1
                msg = "Syntax Error: memory address must be a variable --->line: " + str(cn)
                f2 = open(file2,"a")
                f2.write(msg)
                f2.close()
                return E
            else:
                pass
        cn = cn + 1
    return E
def e_var(L,OP):             # check if var is at the begining 
    E = 0
    c = 0
    j = 0
    for i in L:
        if i == []:
            continue
        if i[0] == 'var':
            j = j + 1
        c = c + 1
        if c != j:
            for k in range(c,len(L)):
                if L[k] == []:
                    continue
                if L[k][0] == 'var':
                    E = 1
                    msg = "Syntax Error: variable not defined at the bebinning --->line: " + str(k+1)
                    f2 = open(file2,"a")
                    f2.write(msg)
                    f2.close()
                    return E
    return E
def e_undef_var(L,OP):   # checks for use of undefined variables
    E = 0
    c = 0
    lst =[]  # variable corresponds to 'var'
    for i in L:
        if i == []:
            continue
        if i[0] == 'var':
            vr = i[1]
            lst.append(vr)
    for i in L:
        if i ==[]:
            c = c + 1
            continue
        elif i[0] in Type_D:
            x = i[2]
            if x not in lst:
                c = c + 1 
                E = 1
                msg = "Syntax Error: Use of undefined variable --->line" + str(c)
                f2 = open(file2,"a")
                f2.write(msg)
                f2.close()
                return E
        elif i[0] in Type_E:
            x = i[1]
            if x not in lst:
                c = c + 1
                E = 1
                msg = "Syntax Error: Use of undefined variable --->line" + str(c)
                f2 = open(file2,"a")
                f2.write(msg)
                f2.close()
                return E
        c = c + 1
    return E
def e_flag(L,OP):
    E = 0
    c = 0
    for i in L:
        if i == []:
            c = c+1
            continue
        elif i[0] in Type_A:
            if i[2] == 'FLAGS' or i[1] == 'FLAGS':
                E = 1
                c = c+1
                msg = "Syntax Error:  Illegal use of FLAGS register ---> line: " + str(c)
                f2 = open(file2,"a")
                f2.write(msg)
                f2.close()
                return E
        elif i[0] in Type_C:
            if (i[0] == 'mov') and (i[1] == 'FLAGS'):
                    E = 1
                    c = c + 1
                    msg = "Syntax Error:  Illegal use of FLAGS register ---> line: " + str(c)
                    f2 = open(file2,"a")
                    f2.write(msg)
                    f2.close()
                    return E
                
            if i[0] != 'mov':
                if i[2] == 'FLAGS' or i[1] == 'FLAGS':
                    E = 1
                    c = c + 1
                    msg = "Syntax Error:  Illegal use of FLAGS register ---> line: " + str(c)
                    f2 = open(file2,"a")
                    f2.write(msg)
                    f2.close()
                    return E
        elif i[0] in Type_B:
            if i[1] == 'FLAGS':
                    E = 1
                    c = c + 1
                    msg = "Syntax Error:  Illegal use of FLAGS register ---> line: " + str(c)
                    f2 = open(file2,"a")
                    f2.write(msg)
                    f2.close()
                    return E                   
        
        elif i[0] in Type_D:
            if i[2] == 'FLAGS' or i[1] == 'FLAGS':
                    E = 1
                    c = c + 1
                    msg = "Syntax Error:  Illegal use of FLAGS register ---> line: " + str(c)
                    f2 = open(file2,"a")
                    f2.write(msg)
                    f2.close()
                    return E   
        elif i[0] in Type_E:
            if i[1] == 'FLAGS':
                    E = 1
                    c = c + 1
                    msg = "Syntax Error:  Illegal use of FLAGS register ---> line: " + str(c)
                    f2 = open(file2,"a")
                    f2.write(msg)
                    f2.close()
                    return E  
        c = c + 1
    return E
def e_typo(L,OP):
    E = 0
    c = 0
    for i in L:
        if i == []:
            c = c + 1
            continue
        elif i[0] != 'var':
            if i[0] !='hlt' and i[0][-1] != ":":
                if (i[0] not in operations):
                    E = 1
                    c = c + 1
                    msg = "Syntax Error: Typo Error in instruction name --->line: " + str(c)
                    f2 = open(file2,"a")
                    f2.write(msg)
                    f2.close()
                    return E  
        c = c + 1
    return E
def e_undf_lebe(L,OP):
    E = 0
    c = 0
    ll = []
    for i in L:
        if i == []:
            continue
        elif i[0][-1] == ":":   # means i[0] is lebel
            ll.append(i[0])
           
        
def errGen(L,OP,operations):
    err = 0
    err = e_hlt(L,OP)
    if err == 1:
        return err
    err = e_imm(L, OP)
    if err == 1:
        return err
    err = e_mem_add(L,OP)
    if err == 1:
        return err
    err = e_var(L,OP)
    if err == 1:
        return err
    err = e_undef_var(L,OP)
    if err == 1:
        return err
    err = e_flag(L,OP)
    if err == 1:
        return err
    err = e_typo(L,OP)
    if err == 1:
        return err
    return err
def output(L,OP,operations):
    ERR = errGen(L,OP,operations)
    if ERR == 0:
        RESULT(L,OP)
output(L,OP,operations)

        
    
    
        
    
                
                
        
            
        
    
                
                
            
            
    
    

                

