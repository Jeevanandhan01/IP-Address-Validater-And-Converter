import re
ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def check_ip_address(user_ip):
   if(re.search(ip_regex, user_ip)):
       return "Valid Ip address"        
   else:
       return "Invalid Ip address"
i1=input("enter the 1st ip address:")
i2=input("enter the 2nd ip address:")
i3=input("enter the 3rd ip address:")
i4=input("enter the 4th ip address:")
i5=input("enter the 5th ip address:")
i6=input("enter the 6th ip address:")
i7=input("enter the 7th ip address:")
i8=input("enter the 8th ip address:")
i9=input("enter the 9th ip address:")
i10=input("enter the 10th ip address:")
print("\n",i1,"-->",check_ip_address(i1))
print("\n",i2,"-->",check_ip_address(i2))
print("\n",i3,"-->",check_ip_address(i3))
print("\n",i4,"-->",check_ip_address(i4))
print("\n",i5,"-->",check_ip_address(i5))
print("\n",i6,"-->",check_ip_address(i6))
print("\n",i7,"-->",check_ip_address(i7))
print("\n",i8,"-->",check_ip_address(i8))
print("\n",i9,"-->",check_ip_address(i9))
print("\n",i10,"-->",check_ip_address(i10))


a1 =  ".".join(map(str,["{0:08b}".format(int(x)) for x in i1.split(".")]))
a2 =  '.'.join(format(int(x), '04o') for x in i1.split('.'))
a3 = '.'.join([hex(int(x)+256)[3:] for x in i1.split('.')])


b1 =  ".".join(map(str,["{0:08b}".format(int(x)) for x in i2.split(".")]))
b2 =  '.'.join(format(int(x), '04o') for x in i2.split('.'))
b3 = '.'.join([hex(int(x)+256)[3:] for x in i2.split('.')])


c1 =  ".".join(map(str,["{0:08b}".format(int(x)) for x in i3.split(".")]))
c2 =  '.'.join(format(int(x), '04o') for x in i3.split('.'))
c3 = '.'.join([hex(int(x)+256)[3:] for x in i3.split('.')])


d1 =  ".".join(map(str,["{0:08b}".format(int(x)) for x in i4.split(".")]))
d2 =  '.'.join(format(int(x), '04o') for x in i4.split('.'))
d3 = '.'.join([hex(int(x)+256)[3:] for x in i4.split('.')])


e1 =  ".".join(map(str,["{0:08b}".format(int(x)) for x in i5.split(".")]))
e2 =  '.'.join(format(int(x), '04o') for x in i5.split('.'))
e3 = '.'.join([hex(int(x)+256)[3:] for x in i5.split('.')])



f1=  ".".join(map(str,["{0:08b}".format(int(x)) for x in i6.split(".")]))
f2 =  '.'.join(format(int(x), '04o') for x in i6.split('.'))
f3 = '.'.join([hex(int(x)+256)[3:] for x in i6.split('.')])


g1 =  ".".join(map(str,["{0:08b}".format(int(x)) for x in i7.split(".")]))
g2 =  '.'.join(format(int(x), '04o') for x in i7.split('.'))
g3 = '.'.join([hex(int(x)+256)[3:] for x in i7.split('.')])


h1 =  ".".join(map(str,["{0:08b}".format(int(x)) for x in i8.split(".")]))
h2 =  '.'.join(format(int(x), '04o') for x in i8.split('.'))
h3 = '.'.join([hex(int(x)+256)[3:] for x in i8.split('.')])


j1 =  ".".join(map(str,["{0:08b}".format(int(x)) for x in i9.split(".")]))
j2 =  '.'.join(format(int(x), '04o') for x in i9.split('.'))
j3 = '.'.join([hex(int(x)+256)[3:] for x in i9.split('.')])


k1 =  ".".join(map(str,["{0:08b}".format(int(x)) for x in i10.split(".")]))
k2 =  '.'.join(format(int(x), '04o') for x in i10.split('.'))
k3 = '.'.join([hex(int(x)+256)[3:] for x in i10.split('.')])

ip1 = [i1,a1,a2,a3]

ip2 = [i2,b1,b2,b3]

ip3 = [i3,c1,c2,c3]

ip4 = [i4,d1,d2,d3]

ip5 = [i5,e1,e2,e3]

ip6 = [i6,f1,f2,f3]

ip7 = [i7,g1,g2,g3]

ip8 = [i8,h1,h2,h3]

ip9 = [i9,j1,j2,j3]

ip10 = [i10,k1,k2,k3]


with open('conversion1.txt','w') as fp1:
    for items in ip1:
        fp1.write('%s\n' % items)
fp1.close()



with open('conversion2.txt','w') as fp2:
    for items in ip2:
        fp2.write('%s\n' % items)
fp2.close()



with open('conversion3.txt','w') as fp3:
    for items in ip3:
        fp3.write('%s\n' % items)
fp3.close()



with open('conversion4.txt','w') as fp4:
    for items in ip4:
        fp4.write('%s\n' % items)
fp4.close()




with open('conversion5.txt','w') as fp5:
    for items in ip5:
        fp5.write('%s\n' % items)
fp5.close()



with open('conversion6.txt','w') as fp6:
    for items in ip6:
        fp6.write('%s\n' % items)
fp6.close()




with open('conversion7.txt','w') as fp7:
    for items in ip7:
        fp7.write('%s\n' % items)
fp7.close()




with open('conversion8.txt','w') as fp8:
    for items in ip8:
        fp8.write('%s\n' % items)
fp8.close()




with open('conversion9.txt','w') as fp9:
    for items in ip9:
        fp9.write('%s\n' % items)
fp9.close()



with open('conversion10.txt','w') as fp10:
    for items in ip10:
        fp10.write('%s\n' % items)
fp10.close()


print("\n\n ----------CONVERSION PART---------")

fp1 = open("conversion1.txt")
fp1_cont = fp1.read()
print("\n\n\n The first ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp1_cont)
fp1.close()


fp2 = open("conversion2.txt")
fp2_cont = fp2.read()
print("The second ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp2_cont)
fp2.close()


fp3 = open("conversion3.txt")
fp3_cont = fp3.read()
print("The third ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp3_cont)
fp3.close()

fp4 = open("conversion4.txt")
fp4_cont = fp4.read()
print("The forth ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp4_cont)
fp4.close()

fp5 = open("conversion5.txt")
fp5_cont = fp5.read()
print("The fifth ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp5_cont)
fp5.close()


fp6 = open("conversion6.txt")
fp6_cont = fp6.read()
print("The sixth ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp6_cont)
fp6.close()

fp7 = open("conversion7.txt")
fp7_cont = fp7.read()
print("The seventh ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp7_cont)
fp7.close()

fp8 = open("conversion8.txt")
fp8_cont = fp8.read()
print("The eighth ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp8_cont)
fp8.close()

fp9 = open("conversion9.txt")
fp9_cont = fp9.read()
print("The nineth ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp9_cont)
fp9.close()

fp10 = open("conversion10.txt")
fp10_cont = fp10.read()
print("The tenth ip4 address in Decimal,Binary,Octal and Hexadecimal format is\n",fp10_cont)
fp10.close()


print("-------------THANKS FOR EXECUTING THIS PROGRAM-------------")


filenames=['conversion1.txt','conversion2.txt','conversion3.txt','conversion4.txt','conversion5.txt','conversion6.txt','conversion7.txt','conversion8.txt','conversion9.txt','conversion10.txt']


with open('conversion.txt','w') as outfile:
    for names in filenames:
    	  with open(names) as infile:
		         outfile.write(infile.read())
		 
