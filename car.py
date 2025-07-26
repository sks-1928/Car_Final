import matplotlib.pyplot as plt
#SO basically the data is stored in simplest List and dictionary Data Structure in python as follows:
#["Car Name",Type,Price,Price range,FuelEfficiency,Sales Unit,Brand,Variant,Features,and in dictionary, reviews]

top_variant_car = [
    ["Hyundai Creta", "SUV", 1800000, "16-20 Lakh", 19, 56000, "Hyundai", "Top",
     ["Full digital cluster", "ADAS", "Sunroof", "Wireless charger"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 4}],
    
    ["Tata Nexon", "SUV", 1450000, "13-15 Lakh", 16.5, 50000, "Tata", "Top",
     ["Sunroof", "Touchscreen", "Wireless charger", "Cruise Control"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 4}],
    
    ["Kia Seltos", "SUV", 1900000, "17-22 Lakh", 14.1, 40000, "Kia", "Top",
     ["LED headlamps", "ADAS", "Bose speakers", "Sunroof"],
     {"Comfort": 5, "Mileage": 3, "Performance": 4, "Maintenance": 4}],
    
    ["Volkswagen Taigun", "SUV", 1974000, "19-20 Lakh", 18.5, 25000, "Volkswagen", "Top",
     ["Electric sunroof", "Ventilated seats", "Touchscreen", "Ambient lighting"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 5}],
    
    ["Maruti Brezza", "SUV", 1600000, "13-18 Lakh", 18.8, 45000, "Maruti Suzuki", "Top",
     ["Heads-up display", "360-degree camera", "LED tail lamps","Sunroof"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 5}],
    
    ["Hyundai i20", "Hatchback", 1125000, "10.5-11.5 Lakh", 15.0, 30000, "Hyundai", "Top",
     ["Wireless charging", "Ambient lighting", "Touchscreen infotainment","Sunroof"],
     {"Comfort": 5, "Mileage": 3.5, "Performance": 4, "Maintenance": 4}],
    
    ["Maruti Swift", "Hatchback", 949000, "9-10 Lakh", 16.0, 40000, "Maruti Suzuki", "Top",
     ["Touchscreen infotainment", "Cruise control", "LED DRLs","16″ alloy wheels"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 5}],
    
    ["Toyota Glanza", "Hatchback", 1000000, "9-10 Lakh", 20.0, 30000, "Toyota", "Top",
     ["Smartplay Pro", "6 airbags", "360 camera","head-up display + push-start"],
     {"Comfort": 4, "Mileage": 4.5, "Performance": 4, "Maintenance": 5}],
    
    ["Hyundai Exter", "Hatchback", 1050000, "9.5-10.5 Lakh", 15.9, 25000, "Hyundai", "Top",
     ["Voice enabled sunroof", "Dashcam", "TPMS","digital cluster"],
     {"Comfort": 5, "Mileage": 3, "Performance": 4, "Maintenance": 4}],
    
    ["Tata Altroz", "Hatchback", 1040000, "9.5-10.5 Lakh", 16.5, 28000, "Tata", "Top",
     ["Touchscreen", "Rain sensing wipers", "iRA connected tech"],
     {"Comfort": 4.5, "Mileage": 3.5, "Performance": 4, "Maintenance": 4}],
    
    ["Hyundai Verna", "Sedan", 1504000, "13.8-15.0 Lakh", 11.1, 20000, "Hyundai", "Top",
     ["ADAS", "Ventilated seats", "Touchscreen", "Bose audio"],
     {"Comfort": 5, "Mileage": 3, "Performance": 4, "Maintenance": 4}],
    
    ["Honda City", "Sedan", 1655000, "15.0-16.6 Lakh", 14.0, 25000, "Honda", "Top",
     ["LaneWatch camera", "Alexa voice commands", "6 airbags","Dual airbags, ABS, and rear parking camera"],
     {"Comfort": 5, "Mileage": 4, "Performance": 5, "Maintenance": 4}],
    
    ["Maruti Ciaz", "Sedan", 1128000, "11.0-12.0 Lakh", 20.5, 18000, "Maruti Suzuki", "Top",
     ["Smart Hybrid", "Cruise control", "LED projector headlamps","cooled glovebox"],
     {"Comfort": 5, "Mileage": 4.5, "Performance": 4, "Maintenance": 5}],
    
    ["Skoda Slavia", "Sedan", 1795000, "17.5-18.5 Lakh", 15.0, 12000, "Skoda", "Top",
     ["Ventilated seats", "Digital cockpit", "Wireless charging","18″ alloy wheels + LED headlamps"],
     {"Comfort": 5, "Mileage": 3.5, "Performance": 5, "Maintenance": 4}],
]

bottom_variant_car = [
    ["Hyundai Creta", "SUV", 1100000, "11-15 Lakh", 17, 13000, "Hyundai", "Bottom",
     ["Touchscreen", "Basic AC", "Rear parking sensors", " All-Wheel Disc Brakes"],
     {"Comfort": 4, "Mileage": 4, "Performance": 4, "Maintenance": 5}],
    
    ["Tata Nexon", "SUV", 799000, "7.5-9 Lakh", 15.0, 200000, "Tata", "Bottom",
     ["Projector headlamps", "Dual airbags", "Power windows","Manual AC with rear AC vents"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 5}],
    
    ["Kia Seltos", "SUV", 1090000, "10.5-12 Lakh", 17.0, 35000, "Kia", "Bottom",
     ["Basic infotainment", "Rear AC vents", "Hill start assist","Manual AC with rear vents"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 4}],
    
    ["Volkswagen Taigun", "SUV", 1170000, "11.5-12 Lakh", 19.9, 30000, "Volkswagen", "Bottom",
     ["Basic infotainment", "LED tail lamps", "Rear wiper"],
     {"Comfort": 4, "Mileage": 4, "Performance": 4, "Maintenance": 4}],
    
    ["Maruti Brezza", "SUV", 869000, "8.5-9 Lakh", 17.38, 60000, "Maruti Suzuki", "Bottom",
     ["Touchscreen", "Auto headlamps", "Electrically adjustable ORVMs","Halogen projector headlamps"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 5}],
    
    ["Hyundai i20", "Hatchback", 700000, "6.8-7.2 Lakh", 17.0, 25000, "Hyundai", "Bottom",
     ["Manual AC", "Basic stereo", "Dual airbags"," ABS"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 4}],
    
    ["Maruti Swift", "Hatchback", 650000, "6.4-6.6 Lakh", 18.5, 50000, "Maruti Suzuki", "Bottom",
     ["Rear defogger", "Adjustable headrests", "Halogen headlamps","Dual airbags + ABS"],
     {"Comfort": 4, "Mileage": 4, "Performance": 4, "Maintenance": 4}],
    
    ["Toyota Glanza", "Hatchback", 685000, "6.8-7.0 Lakh", 22.3, 25000, "Toyota", "Bottom",
     ["Infotainment system", "Electrically foldable mirrors", "Keyless entry","14″ steel wheels"],
     {"Comfort": 4, "Mileage": 4, "Performance": 4, "Maintenance": 5}],
    
    ["Hyundai Exter", "Hatchback", 620000, "6.2-6.5 Lakh", 12.0, 20000, "Hyundai", "Bottom",
     ["ABS with EBD", "Speed alert", "Manual AC","2-DIN audio + basic MID"],
     {"Comfort": 4, "Mileage": 3, "Performance": 4, "Maintenance": 4}],
    
    ["Tata Altroz", "Hatchback", 689000, "6.8-7.1 Lakh", 19.3, 30000, "Tata", "Bottom",
     ["Tilt steering", "Flat-bottom wheel", "Dual airbags""4.2″ MID",],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 4}],
    
    ["Hyundai Verna", "Sedan", 1380000, "13.5-14.0 Lakh", 12.0, 15000, "Hyundai", "Bottom",
     ["LED DRLs", "Touchscreen", "Voice control","8″ touchscreen infotainment"],
     {"Comfort": 4, "Mileage": 3, "Performance": 4, "Maintenance": 4}],
    
    ["Honda City", "Sedan", 1228000, "12.0-12.5 Lakh", 13.5, 20000, "Honda", "Bottom",
     ["Cruise control", "Keyless entry", "Auto AC","Eco Drive Indicator"],
     {"Comfort": 4, "Mileage": 3.5, "Performance": 4, "Maintenance": 4}],
    
    ["Maruti Ciaz", "Sedan", 941000, "9.4-9.6 Lakh", 16.0, 10000, "Maruti Suzuki", "Bottom",
     ["Touchscreen", "Auto climate", "Steering controls","Manual AC with rear vents"],
     {"Comfort": 4, "Mileage": 4, "Performance": 4, "Maintenance": 5}],
    
    ["Skoda Slavia", "Sedan", 1069000, "10.5-11.0 Lakh", 18.7, 8000, "Skoda", "Bottom",
     ["Cruise control", "Rear AC vents", "Digital display","6 airbags, TPMS, ESC"],
     {"Comfort": 4, "Mileage": 4, "Performance": 4, "Maintenance": 4}],
]



#A certain weightage is given to all crietria and score is calculated 

def calculate_score(car):
    reviews = car[9]
    comfort = reviews["Comfort"]
    mileage = reviews["Mileage"]
    performance = reviews["Performance"]
    maintenance = reviews["Maintenance"]

    fuel_efficiency = car[4]  
    sales = car[5]            

    
    fuel_score = fuel_efficiency / 5
    if fuel_score > 5:
        fuel_score = 5

    sales_score = sales / 10000
    if sales_score > 5:
        sales_score = 5

    total = (comfort + mileage + performance + maintenance + fuel_score + sales_score) / 6
    return round(total, 2)




all_car = top_variant_car + bottom_variant_car #List are combine to one


print("WELCOME TO AI BASED CAR RECOMMENDATION SYSTEM\n")
print("WELCOME TO AI BASED CAR RECOMMENDATION SYSTEM\n")

# Step 1: Car type selection
valid_types = ["hatchback", "sedan", "suv"]
selected = input("Enter car type (Hatchback / Sedan / SUV): ").strip().lower()

if selected not in valid_types:
    print("❌ Invalid car type entered. Please enter one of: Hatchback, Sedan, SUV")
    exit()

# Step 2: Budget options
if selected == "hatchback":
    budgets = ["6-8 Lakh", "8-10 Lakh", "10-12 Lakh"]
elif selected == "sedan":
    budgets = ["8-10 Lakh", "10-12 Lakh", "11-14 Lakh", "14-16 Lakh", "16-18 Lakh"]
elif selected == "suv":
    budgets = ["6-8 Lakh", "8-10 Lakh", "10-14 Lakh", "14-16 Lakh", "16-18 Lakh", "18-20 Lakh"]

print("\nSelect your budget:")
for i, b in enumerate(budgets):
    print(f"{i+1}. {b}")

budget_index = int(input("Enter option number: ")) - 1
selected_budget = budgets[budget_index]


budget_range = selected_budget.replace("Lakh", "").split("-")
min_budget = float(budget_range[0]) * 100000
max_budget = float(budget_range[1]) * 100000

print(f"\n✅  You selected: {selected} with budget {selected_budget} (₹{int(min_budget):,} to ₹{int(max_budget):,})")

#Cars with matched criteria

matched_cars = []
for car in all_car:
    if car[1].lower() == selected.lower() and min_budget <= car[2] <= max_budget:
        score = calculate_score(car)
        matched_cars.append((car, score))

matched_cars.sort(key=lambda x: x[1], reverse=True)

#  Display Results
if not matched_cars:
    print("\n No matching cars found for your criteria.")
else:
    print("\nTop Car Recommendations:\n")
    for car, score in matched_cars:
        print(f" 🚗  Name: {car[0]}")
        print(f"     Type: {car[1]}")
        print(f"     Price: ₹{car[2]:,}")
        print(f"     Variant: {car[7]}")
        print(f"     Score: {score}/5")
        print(f"     Mileage: {car[4]} km/l")
        print(f"     Sales: {car[5]}")
        print(f"     Features: {', '.join(car[8])}")
        reviews = car[9]
        print(f"     Reviews → Comfort: {reviews['Comfort']}, Mileage: {reviews['Mileage']}, "
              f"Performance: {reviews['Performance']}, Maintenance: {reviews['Maintenance']}")
        print("-" * 50)

   
    best_car = max(matched_cars, key=lambda x: x[1])
    print(f"\n✅  Best Recommended Car: {best_car[0][0]} (Score: {best_car[1]}/5)")

 #Graph Plot
    show = input("\nDo you want to see comparison graph? (yes/no): ").strip().lower()
    if show in ['yes', 'y']:
        names = [car[0][0] for car in matched_cars]
        scores = [car[1] for car in matched_cars]
        sales = [car[0][5] for car in matched_cars]

        plt.figure(figsize=(13, 6))

        # Scores
        plt.subplot(1, 2, 1)
        plt.bar(names, scores, color='lightgreen')
        plt.ylabel("Score (/5)")
        plt.title("Car Recommendation Scores")
        plt.xticks(rotation=30, ha='right')

        # Sales
        plt.subplot(1, 2, 2)
        plt.bar(names, sales, color='coral')
        plt.ylabel("Units Sold")
        plt.title("Car Sales Volume")
        plt.xticks(rotation=30, ha='right')

        plt.tight_layout()
        plt.show()
    else:
        print("Exit")    
