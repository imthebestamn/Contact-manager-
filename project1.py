import json

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    
    person = {"Name": name, "Age": age, "Email": email}
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-",person['Name'], "|",person["Age"], "|", person["Email"])

def delete_contact(people):
    display_people(people)
    
    while True:
        number =  input("Enter a number to delete a person: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range")
            else:
                break
        except:
            print("Invalid number")
            
    people.pop(number - 1)
    print("Person deleted successfully.")
    
def search(people):
    search_name  = input("Search for a name:").lower()
    results = []
    
    for person in people:
        name = person["Name"]
        if search_name in name.lower():
            results.append(person)
    
    display_people(results)
    
print("hi, welcome to the Contact Manager System.")
print()

with open("contact.json", "r") as f:
    people = json.load(f)["contact"]

# people = []
 
while True:
   print()
   print("Contact List Size:", len(people))
   
   
   command = input("you can 'Add', 'Delete', or 'Search', and 'Quit':").lower()
  

   if command == "add":
       person = add_person()
       people.append(person)
       print("Person added successfully.")
   elif command == "delete":
       delete_contact(people)
   elif command == "search":
       search(people)
   elif command == "quit":
       break
       print("Goodbye!")
   else:
       print("invalid command")

print(people)

with open("contact.json", "w") as f:
    json.dump( {"contact": people}, f)
