import random
import os

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

def dice():
    x = "y"
    while x == 'y':
        no = random.randint(1, 6)
        if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
            break
        elif no == 2:
            print("[-----]")
            print("[     ]")
            print("[0   0]")
            print("[     ]")
            print("[-----]")
            break
        elif no == 3:
            print("[-----]")
            print("[  0  ]")
            print("[0   0]")
            print("[     ]")
            print("[-----]")
            break
        elif no == 4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
            break
        elif no == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
            break
        elif no == 6:
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print("[-----]")
            break
dice()
res = str(input("\nDo you want to try again? "))

while res:
    if res.lower() == "y":
     dice()
     res = str(input("\nDo you want to try again? "))
    else:
        quit()

