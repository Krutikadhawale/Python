car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

del car["color"]

print(car)

if "brand" in car:
    print("Brand key exists")
else:
    print("Brand key does not exist")