number = int(input("Number to be checked:"))
print("Checking the number wheater its even or oddd")

if number%2==0:
    print("Number is even")

else:
    print("Number is odd")

#Elif statent (bmi calculator)

height = float(input("Enter your height in cm"))
weight = float(input("Enter your weight in kg"))

BMI = weight/(height/100)**2

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
  print("ou are healthy")
elif BMI <= 30.2:
  print("You are overweight")
elif BMI <= 34.5:

  print("You are obese")

#Nested conditional

number = int(input("Number is :"))

if number>50:
  print("Number is :",number)
  if number%2==0:
    print("AND number is even")
  else:
      print("and number is odd")

else:
  print("Number is less than 50")

#datetime module 

import datetime
current_time=datetime.datetime.now()
print("The time in Pakistan right now is:")
print(current_time)

#calender module

import calendar
print("n/",calendar.calendar(2011))4