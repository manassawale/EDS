from datetime import datetime

f1=open("empsal.csv","r")
c=f1.read()
data=c.splitlines()

eid=[]
name=[]
pos=[]
loc=[]
sal=[]
dob=[]

for line in data:
    word=line.split(",")
    eid.append(int(word[0]))
    name.append(word[1])
    pos.append(word[2])
    loc.append(word[3])
    sal.append(int(word[4]))
    dob.append(word[5])

print("MAXIMUM SALARY :",name[sal.index(max(sal))],max(sal))
print("MINIMUM SALARY :",name[sal.index(min(sal))],min(sal))
print("TOTAL SALARY :",sum(sal))
print("AVERAGE SALARY :",(sum(sal)/len(eid)))

today=datetime.today()

for d in dob:
      ed=datetime.strptime(d,'%m/%d/%Y').date()
      print("AGE OF EMP :",(today.year-ed.year))
for s in sal:
    sd=s/82
    print("SALARY IN DOLLARS :",sd,"$")
