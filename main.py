import pickle
import os

f_name = input("filename: ")+".goals"
def add_goals():
  d = {}
  if(os.path.exists(f_name)):
    f = open(f_name, "rb")
    if(f):
      d = pickle.load(f)
    f.close()
  with open(f_name, "wb") as file:
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
    p = 0
    for k,v in obj.items():
      print(f"\033[35mgoal\033[0m {k} : completion {'\033[92m' if v == True else '\033[31m'}{"completed" if v == 1 else "not completed"}\033[0m \n \n ")
      if v == 1:
        p+=1
    completion = int((p/(len(obj))) * 100)
    print(f"\033[35mcompletion: {completion}%\033[0m")

def modify_goals():
  d = {}
  f = open(f_name, "rb")
  d = pickle.load(f)
  autosave = d.copy()
  f.close()
  with open(f_name ,"wb") as file:
    while True:
      try:
        feild = input("what feild do you want to modify: ")
        val = int(input("1/0"))
        d[feild] = val
        c = input("do you want to continue to modify(y/n): ")
        if c == "n":
          break
      except:
        pickle.dump(autosave, file)
        return
        
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
