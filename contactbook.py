name = []
phone_number = []
num =3

for i in range(num):
    name =input("Name: ")
    phone_number =input("Phone Number:")
    name.append(name)
    phone_number.append(phone_number)

print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(name[i], phone_number[i]))

search_term =input("\nEnter Search Term")
print("Search Result")
if search_term in name:
    index= name.index(search_term)
    phone_number=phone_number[index]
    print("Name:{}, Phone Number:{}".format(search_term, phone_number))
else:
    print("Name not found")
