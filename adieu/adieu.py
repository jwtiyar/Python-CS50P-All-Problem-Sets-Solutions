import inflect
p = inflect.engine()
mylist = []
while True:
    try:
        Naw = input("Name: ")
        texste = "Adieu, adieu, to "
        mylist.append(Naw)
    except EOFError:
        print(f"Adieu, adieu, to {p.join(mylist)}")
        break
