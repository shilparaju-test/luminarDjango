from re import *
f=open("registrationumbers","r")
fout=open("vehcilenum","w")
regnum =set()#avoiding duplicate values
for numbers in f:
    regnum.add(numbers.rstrip("\n"))
#print(regnum)
rule="KL[\d]{2}[A-Z]{1,2}\d{1,4}"
for vehnum in regnum:
    matcher=fullmatch(rule,vehnum)
    if matcher!=None:
        fout.write(vehnum+"\n")
    else:
        pass
