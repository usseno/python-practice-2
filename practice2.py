driver = input("Enter driver name: ")
destination = input("Enter destination: ")
distance = float(input("Enter distance (km): "))
consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))

litres_needed = distance * consumption / 100
fuel_cost = litres_needed * fuel_price

if distance < 100:
    category='Short trip'
elif distance < 500:
    category='Medium trip'
else:
    category='Long trip'

print("=" * 30)
print("      ROAD TRIP SUMMARY")
print("=" * 30)

print("Driver :", driver)
print("Destination :", destination.upper())
print("Distance :", distance, "km")
print("Fuel cost :", fuel_cost, "KZT")
print("Category :", category)
print("=" * 30)


print('Cost Breakdown:')
step_cost = 100 * consumption / 100 * fuel_price
for km in range(100,int(distance),100):
    cost_so_far=km*consumption/100*fuel_price
    print(km,"km ->", cost_so_far,"KZT")

print("Destination uppercase :", destination.upper())
print("Destination lowercase :", destination.lower())
print("Length :", len(destination))
print("Letter 'a' count :", destination.lower().count("a"))
