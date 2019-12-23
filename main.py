c = {}
program = {}
values = {}
b = 1

obj = open("register.txt","r")
for line in obj:
   line = line.strip()
   zuordnung = line.split(" ")
   c[int(zuordnung[0])] = zuordnung[1]
obj.close()

obj = open("code.txt","r")
for line in obj:
   line = line.strip()
   zuordnung = line.split(" ")
   program[int(zuordnung[0])] = zuordnung[1]
   values[int(zuordnung[0])] = zuordnung[2]
obj.close()

def load(x):
   global b
   c[0]=c[x]
   b+=1
def store(x):
   global b
   c[x]=c[0]
   b+=1
def add(x):
   global b
   c[0]=c[0]+c[x]
   b+=1
def sub(x):
   global b
   c[0]=c[o]-c[x]
   if c[0]<0:
      c[0]=0
   b+=1
def mult(x):
   global b
   c[0]=c[0]*c[x]
   b+=1
def div(x):
   global b
   c[0]=c[0]/c[x]
   b+=1
def jump(x):
   global b
   b = x
def jzero(x):
   global b
   if c[0]==0:
      b=x
def jge(x):
   global b
   if c[0]>0:
      b=x
def iload(x):
   global b
   c[0]=c[c[x]]
   b+=1
def cload(x):
   global b
   c[0]=x
   b+=1
def cadd(x):
   global b
   c[0]+=x
   b+=1
def end(x):
   global b
   b+=1
def run(x):
   print("Step: ",x)
   code = program[x] + "(" + values[x] + ")"
   print("Code: ",code)
   eval(code)
   print(c)
   print("#######################################")

laenge = len(program)

while b<=laenge:
   run(b)

print("Fertig!");
