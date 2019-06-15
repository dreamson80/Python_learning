def seconds_minutes_to_hours(seconds=0, minutes=0):
    hours = seconds / 3600 + minutes / 60
    #print (hours)
    return (hours)
#print(type(seconds_minutes_to_hours(7200,90)))
#print(seconds_minutes_to_hours(7200,90))
#seconds_minutes_to_hours(7200,90) + 10
print(seconds_minutes_to_hours(7200,90)+10)
