#Description:
#1-Write a Python program that prints the corresponding season based on the value of the variable season_num.
#2-The possible values of season_num are: 1 for Spring, 2 for Summer, 3 for Fall, 4 for Winter.
#3-If the value of season_num is neither one of these values, print "Please enter a valid number".

season_num=0
corresponding_season=''
while True:
    season_num=int(input("Type in a season_number: "))
    if season_num in [1,2,3,4]:
        break
match season_num:
    case 1:corresponding_season='Spring'
    case 2:corresponding_season='Summer'
    case 3:corresponding_season='Fall'
    case _:corresponding_season='Winter'

print('{form} corresponds to: {season}'.format(form=season_num,season=corresponding_season))