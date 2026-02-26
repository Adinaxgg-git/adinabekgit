# json.py
import json

# Load JSON file
with open("sample-data.json", "r") as f:
    data = json.load(f)

# Exercise 1: Print interface table
print("Interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-"*80)

for item in data:
    dn = item.get("dn", "")
    desc = item.get("description", "")
    speed = item.get("speed", "")
    mtu = item.get("mtu", "")
    print(f"{dn:<50} {desc:<20} {speed:<6} {mtu:<6}")