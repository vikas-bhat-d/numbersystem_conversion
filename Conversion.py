l=list()
l2=list()
global il
il=list()
il2=list()
value=dict()
value={"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}



"""
no=int(input("Enter a decimal number  "))
dec=no
n=1
while(dec>0):
    dec=int(dec/2)
    print(dec)

def binaryconversion(dec,n):
    

    while(n==1):
        rem=dec%2
        #print(rem)
        dec=int(dec/2)
        if(dec==0):
            n=0
        else:
            n=1
        l.append(rem)
    #print(l)
    i=len(l)-1
    while(i>=0):
        il.append(str(l[i]))
        i-=1
    binarydigit="".join(il)
    return binarydigit
def octalconversion(dec,n):
    

    while(n==1):
        rem=dec%8
        #print(rem)
        dec=int(dec/8)
        if(dec==0):
            n=0
        else:
            n=1
        l2.append(rem)
    #print(l)
    i=len(l2)-1
    while(i>=0):
        il2.append(str(l2[i]))
        i-=1
    octaldigit="".join(il2)
    return octaldigit
binary=binaryconversion(dec,n)
octal=octalconversion(dec,n)
print("\n")
print("The binary of {0} is {1}\n\n".format(no,binary))
print("The octal of {0} is {1}\n\n".format(no,octal))
"""
rem=14
print(value[str(rem)])