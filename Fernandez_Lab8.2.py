##Robert Fernandez
##Complete
##This program will read a string from the user containing a date in the form mm/dd/yyyy. It should print the date in the format March 12, 2018.

#This will ask the user to input a date in the form mm/dd/yyyy
date = input("Enter a date in the form mm/dd/yyyy: ")

#This will split the date into the month, day, and year
month = date[0:2]
day = date[3:5]
year = date[6:10]

#This will convert the month into a word
if month == "01":
  month = "January"

elif month == "02":
  month = "February"

elif month == "03":
  month = "March"

elif month == "04":
  month = "April"

elif month == "05":
  month = "May"

elif month == "06":
  month = "June"

elif month == "07":
  month = "July"

elif month == "08":
  month = "August"

elif month == "09":
  month = "September"

elif month == "10":
  month = "October"

elif month == "11":
  month = "November"

elif month == "12":
  month = "December"

#This will print the date in the form of month day, year

print(month, day + ",", year)
