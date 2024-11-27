ram_age = int(input("Enter the age of Ram: "))
sulabh_age = int(input("Enter the age of Sulabh: "))
ajay_age = int(input("Enter the age of Ajay: "))
if ram_age < sulabh_age and ram_age < ajay_age:
    print("Ram is the youngest")
elif sulabh_age < ram_age and sulabh_age < ajay_age:
    print("Sulabh is the youngest")
else:
    print("Ajay is the youngest")