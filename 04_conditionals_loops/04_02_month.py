'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

num=int(input('Write the number of the month'))
if 0<num<=12:
    if num==1:
        print('January')
    if num==2:
        print('February')
    if num==3:
        print('March')
    if num==4:
        print('April')
    if num==5:
        print('May')
    if num==6:
        print('June')
    if num==7:
        print('July')
    if num==8:
        print('August')
    if num==9:
        print('September')
    if num==10:
        print('October')
    if num==11:
        print('November')
    if num==12:
        print('December')
else:
    print('Other')