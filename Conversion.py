lhs=list()
lhs2=list()
ilhs=list()
ilhs2=list()
lhs3=list()
ilhs3=list()

value=dict()
value={"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}


no=int(input("Enter a decimal number  "))
dec=no
n=1

def binaryconversion(dec,n):
    

    while(n==1):
        rem=dec%2
        #print(rem)
        dec=dec//2
        if(dec==0):
            n=0
        else:
            n=1
        lhs.append(rem)
    #print(l)
    i=len(lhs)-1
    while(i>=0):
        ilhs.append(str(lhs[i]))
        i-=1
    binarydigit="".join(ilhs)
    return binarydigit

def octalconversion(dec,n):
    

    while(n==1):
        rem=dec%8
        #print(rem)
        dec=dec//8
        if(dec==0):
            n=0
        else:
            n=1
        lhs2.append(rem)
    #print(l)
    i=len(lhs2)-1
    while(i>=0):
        ilhs2.append(str(lhs2[i]))
        i-=1
    octaldigit="".join(ilhs2)
    return octaldigit

def hexadecimalconv(dec,n,value):
    
    while(n==1):
        rem=dec%16
        dec=dec//16
        if(dec==0):
            n=0
        else:
            n=1
        lhs3.append(value[str(rem)])
        #print(value[str(rem)])
    i=len(lhs3)-1
    while(i>=0):
        ilhs3.append(lhs3[i])
        i-=1
    hexadecimal="".join(ilhs3)
    return hexadecimal
binary=binaryconversion(dec,n)
octal=octalconversion(dec,n)
hexa=hexadecimalconv(dec,n,value)

response=int(input("Enter to which number system you want to it convert...\n(1:binary   2:octal  3:hexadecimal   4:all three)\n\n"))
if(response==1):
    print("\nThe binary of {0}\u2081\u2080 is {1}\u2082\n\n".format(no,binary))
elif(response==2):
    print("\nThe octal of {0}\u2081\u2080 is {1}\u2088\n\n".format(no,octal))
elif(response==3):
    print("\nThe hexadecimal of {0}\u2081\u2080 is {1}\u2081\u2086\n\n".format(no,hexa))
elif(response==4):
    print("\nThe binary of {0}\u2081\u2080 is {1}\u2082\n\n".format(no,binary))
    print("\nThe octal of {0}\u2081\u2080 is {1}\u2088\n\n".format(no,octal))
    print("\nThe hexadecimal of {0}\u2081\u2080 is {1}\u2081\u2086\n\n".format(no,hexa))
else:
    print("\ninvalid input")
