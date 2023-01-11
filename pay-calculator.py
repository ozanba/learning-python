hour = input("how many hours you work: ")
hourly = input("Hourly wage: ")
fhour = float(hour)
fhourly = float(hourly)
#if he works more than 6 hours  he gets more paid.
if fhour>6.0:
    pay = fhourly * 6 + (fhour-6)*1.5*fhourly
else:
    pay = fhourly * fhour

print("daily= ",pay)
print("weekly= ", pay*7)