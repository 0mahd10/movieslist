#movielist :

movielist = ["happy death day" , "get out"]
movielist.pop()


movielist.insert(0 , "star wars 5")
movielist.insert(2 , "astroid city")

movielist.pop(0)


movielist.insert(0, "portrait of a lady on fire")

def space():
    print("--------------------------------------------------")

print("list of movies:")

print(movielist)

space()




print(f"first of list: {movielist[0]}")
space()


if movielist[0] == "portrait of a lady on fire":
    for i in range(2):
        print(f"today movie is: {movielist[0]}")
        space()
  
 

if movielist[0] == "happy death day":
   for i in range(3):
     print("you can buy it another time, this is not your choise")
     space()



if movielist[0] ==" ":
    for i in range(2):
        print("nothing for today")
        space()




# THIS list gonna update