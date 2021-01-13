from re import *
f=open("emails","r")
fout=open("validemail","w")
emailset=set()
for mail in f:
    emailset.add(mail.rstrip("\n"))
#print(emailset)
rule='[a-z0-9][@][a-z][.]w'
for validmail in emailset:
    #print(validmail)
    matcher=fullmatch(rule,"validmail")
    if matcher!=None:
        fout.write(validmail+"\n")
    else:
        pass