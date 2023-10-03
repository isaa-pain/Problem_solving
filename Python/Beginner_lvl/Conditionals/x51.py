#Description:
#1-Write a Python program that prints the number of days in a given month.
#2-The value of the variable month is the name of the month with the first letter capitalized.
#3-Do not consider leap years for the number of days in February.
#4-You can add a customized message. For example: "<month> has: <num_days> days."

month=input("Type in a month: ")
days_number=0
match month:
    case 'January':days_number=31
    case 'February':days_number=28
    case 'March':days_number=31
    case 'April':days_number=30
    case 'May':days_number=31
    case 'June':days_number=30
    case 'July':days_number=31
    case 'August':days_number=31
    case 'September':days_number=30
    case 'October':days_number=31
    case 'November':days_number=30
    case _:days_number=31
print("The month {form} has: {days}".format(form=month,days=days_number))