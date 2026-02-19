import json

# Python dictionary
data = {
    "name": "Adina",
    "age": 18,
    "city": "Almaty"
}

# Convert Python → JSON
json_string = json.dumps(data, indent=4)
print(json_string)

# Write JSON file
with open("sample-data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read JSON file
with open("sample-data.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded:", loaded_data)
