pos = -1

def search (list, x):
    i = 0

    while i < len(list) :

        if list[i] == x :
            globals() ['pos'] = i
            return True
        i = i + 1
    else:
        return False

list = [2,5,8,6,10,45]
x = 7

if search(list, x):
    print ("Found at ", pos+1)
else:
    print("Not Found")
