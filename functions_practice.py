def hello():
    print ("hello user")
hello()    

def pack_numbers():
    list = []
    for i in range (0, 20):
        list.append(i)
    return list
L = pack_numbers()
print (L)

def eat_lunch(my_food):
    if len(my_food) == 0:
        print("my lunchbox is empty")
    else:
        for i in range(len(my_food)):
            if i == 0:
                print(f"first i eat {my_food[1]}")
            else: print(f"after that i eat {my_food[i]}")

eat_lunch([])

eat_lunch(["bagel", "oatmeal" , "coffee", "wheat bar"])






