#movielist :
others = ["convent", "mr.robot", "american hustle"]


movielist = []

def seen():
    movielist.pop(0)

def choiser():
    movielist.insert(0, others[0])
    others.pop(0)

def change():
    seen()
    choiser()


movielist.insert(0, "portrait of a lady on fire")

def space():
    print("--------------------------------------------------")

print("list of movies:")

print(movielist)

space()




print(f"first of list: {movielist[0]}")
space()


if movielist[0] == others[0]:
    for i in range(2):
        print(f"today movie is: {movielist[0]}")
        space()
  
 

if movielist[0] == others[1]:
   for i in range(3):
     print("you can buy it another time, this is not your first choise")
     space()



if movielist[0] ==" ":
    for i in range(2):
        print("nothing for today")
        space()




# THIS list gonna update
