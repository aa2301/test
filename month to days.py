def day(month):
    a=["January","March","May","July","August","October","December"]
    b=["April","June","September","November"]
    if month in a:
        return "31 days"
    elif month in b:
        return "30 days"
    else:
        return "28/29 days"
print("List of month: ","January,","Februray,","March,","April,","May,","June,","July,","August,","September,","October,","November,","December")
print("Enter the month: ")
a=input()
print("Number of days: ",day(a))