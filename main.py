import pickle
f_name = input("filename: ")+".goals"
def add_goals():
  d = {}
  f = open(f_name, "rb")
  d = pickle.load(f)
  f.close()
  with open(f_name, "wb+") as file:
    n = {}
    goals = []  
    file.seek(0,2)
    i = int(input("num of checks: "))
    while i > 0:
      check = input("add check: ")
      goals.append(check)
      i-=1;
      if(i == 0):
        c = input("any extra checks you want to add(y/n): ")
        if c == "y":
          i+=1
    d.update(n.fromkeys(goals, False))
    pickle.dump(d, file)
      
def check_goals():
  with open(f_name, "rb") as file:
    obj = pickle.load(file)
    for k,v in obj.items():
      print(f"\033[35mgoal\033[0m {k} : completion {'\033[92m' if v == True else '\033[31m'}{v}\033[0m \n \n ")

def modify_goals():
  d = {}
  f = open(f_name, "rb")
  d = pickle.load(f)
  f.close()
  with open(f_name ,"wb") as file:
    while True:
      feild = input("what feild do you want to modify: ")
      val = int(input("1/0"))
      d[feild] = val
      c = input("do you want to continue(y/n): ")
      if c == n:
        break
    pickle.dump(d, file)

while True:
  c = int(input("do you want to (1)check, (2) add, (3) modify: "))
  if c == 1:
    check_goals()
  elif c == 2:
    add_goals()
  else:
    modify_goals()
  
  y = input("do you want to continue(y/n): ")
  if y == "n":
    break
