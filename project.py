# Sample database of locations and their green tech features
locations = [
    {"name": "Solar Valley Campus", "features": ["solar power", "EV charging"]},
    {"name": "WindTech Research Lab", "features": ["wind turbines"]},
    {"name": "City Library", "features": ["LED lighting"]},
    {"name": "EcoMall", "features": ["solar panels", "green roofing", "EV charging"]},
    {"name": "Downtown Office Park", "features": ["none"]},
]

# Define green tech keywords
green_tech_features = ["solar", "wind", "EV", "green", "LED"]

# Function to identify green tech sites
def find_green_tech_sites(locations):
    green_sites = []
    for loc in locations:
        if any(any(gf.lower() in f.lower() for gf in green_tech_features) for f in loc["features"]):
            green_sites.append(loc)
    return green_sites

# Run the program
green_sites = find_green_tech_sites(locations)

# Output
print("Green Tech Sites Found:")
for site in green_sites:
    print(f"- {site['name']}: {', '.join(site['features'])}")
