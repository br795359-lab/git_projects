patients = {}

def add_patient():
    pid = input("Enter Patient ID: ")
    if pid in patients:
        print("Patient already exists!")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    doctor = input("Enter Doctor Name: ")

    patients[pid] = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease,
        "Doctor": doctor
    }
    print("Patient added successfully!")

def view_patient():
    pid = input("Enter Patient ID: ")
    if pid in patients:
        print("\nPatient Details:")
        for key, value in patients[pid].items():
            print(f"{key}: {value}")
    else:
        print("Patient not found!")

def update_patient():
    pid = input("Enter Patient ID: ")
    if pid in patients:
        print("Enter new details:")
        patients[pid]["Name"] = input("Name: ")
        patients[pid]["Age"] = input("Age: ")
        patients[pid]["Gender"] = input("Gender: ")
        patients[pid]["Disease"] = input("Disease: ")
        patients[pid]["Doctor"] = input("Doctor: ")
        print("Patient record updated!")
    else:
        print("Patient not found!")

def delete_patient():
    pid = input("Enter Patient ID: ")
    if pid in patients:
        del patients[pid]
        print("Patient deleted successfully!")
    else:
        print("Patient not found!")

def menu():
    while True:
        print("\n--- Hospital Patient Management System ---")
        print("1. Add Patient")
        print("2. View Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patient()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

menu()
