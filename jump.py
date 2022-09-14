Number = int(input("enter the number to be mirror: "))
mirror_Number = 0
while(Number > 0):
 Reminder = Number %10
 mirror_Number = (mirror_Number *10) + Reminder
 Number = Number //10
print("mirror of the given number is = %d" %mirror_Number)
