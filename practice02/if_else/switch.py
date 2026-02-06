#1
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Fail"

#2
choice = 3

if choice == 1:
    print("Add item")
elif choice == 2:
    print("Delete item")
elif choice == 3:
    print("View items")
else:
    print("Invalid choice")

#3
light = "yellow"

if light == "red":
    action = "Stop"
elif light == "yellow":
    action = "Slow down"
elif light == "green":
    action = "Go"
else:
    action = "Broken signal"

#4
day = "Sunday"

if day in ["Saturday", "Sunday"]:
    type = "Weekend"
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    type = "Weekday"
else:
    type = "Invalid day"

#5
username = "admin"
password = "1234"

if username != "admin":
    print("Unknown user")
elif password != "1234":
    print("Wrong password")
else:
    print("Login successful")

