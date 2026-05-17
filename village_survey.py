class Villager:
    def __init__(self, name, age, gender, occupation, income):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.income = income

    def display(self):
        print("\n--- Villager Details ---")
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Occupation :", self.occupation)
        print("Income     :", self.income)

village_data = []

while True:
    print("\n===== Village Survey System =====")
    print("1. Add Villager Record")
    print("2. View All Records")
    print("3. Search Villager")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        occupation = input("Enter Occupation: ")
        income = float(input("Enter Monthly Income: "))

        villager = Villager(name, age, gender, occupation, income)
        village_data.append(villager)

        print("Record Added Successfully!")

    elif choice == "2":
        if len(village_data) == 0:
            print("No records found.")
        else:
            for v in village_data:
                v.display()

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for v in village_data:
            if v.name.lower() == search_name.lower():
                v.display()
                found = True
                break

        if not found:
            print("Villager not found.")

    elif choice == "4":
        print("Exiting Village Survey System...")
        break

    else:
        print("Invalid Choice! Please try again.")
