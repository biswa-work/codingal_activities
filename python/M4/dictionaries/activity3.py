# Activity 3: Get the Country Code

country_code = {
    "India": "+91",
    "USA": "+1",
    "Japan": "+81"
}

country = input("Enter a country: ")

code = country_code.get(country, "Country not found")

print("Dialing code:", code)
