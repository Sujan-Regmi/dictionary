l = eval(input("Enter a list: "))
e = int(input("Enter an element to remove: "))

flag = 0

while True:
    if e in l:
        l.remove(e)
        flag = 1
    else:
        print(l)
        break

if flag == 0:
    print("Element does not exist")