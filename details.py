names = []
def storename():
    name=input("Enter the name to be saved:")
    name=name.strip().title()
    names.append(name)
    return name

def listnames():
    print("*"*30)
    print("names in the list")
    print("*"*30)
    for name in names:
        print(name)
        print("*"*30)

def searchname(search):
    search = search.strip().title()
    found = False
    for name in names:
        if name == search:
            found=True
            break
    if found == True:
            print("name exists in the list:")
    else:
        print("Name does not exist..!")

while True:
    print("*"*30)
    print("1. Enter a Name")
    print("2. List the Names")
    print("3. Search for a Name")
    print("4. Exit")
    print("*"*30)

    choice=int(input("Enter your choice"))
    print ("you have entered choice:",choice)
    

    if (choice) ==  1:
        name = storename()
        print("name{} added successfully!".format(name))
    elif (choice) == 2:
        listnames()
    elif (choice) == 3:
        name=input("enter name to be searched")
        searchname(name)
    elif (choice) == 4:
        break
    else:
        print("invalid option") 