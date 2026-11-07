player = ["Arian","Reza","Ali","Amir","Korosh"]
role = ["god father","mofia","dr","Citizen","Detective"]
import random
for i in player :
    item = random.choice(role)
    print(i,"=>",item)
    role.remove(item)
