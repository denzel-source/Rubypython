 # Create a Program that Checks a Student's Performance
marks =int(input("Enter Marks"))

if 100 >=marks>=80:
    print("You have an A")
elif 79>=marks>=60:
   print("You have a B")
elif 59>=marks>= 40:
    print("You have a C")
elif 39>=marks>=0:
    print("You have failed,please try again")
else:
    print("Invalid entry")
