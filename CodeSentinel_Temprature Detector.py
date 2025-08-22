# Temperature Converter Program

# Ask the user for input
temp = input("Enter temperature (e.g., 37C or 98F): ").strip()

# Get the numeric part and the scale
value = float(temp[:-1])   # all characters except last one
scale = temp[-1].upper()   # last character (C or F)

# Check the scale and convert
if scale == "C":
    converted = (value * 9/5) + 32
    print(f"{value}°C is equal to {converted:.2f}°F")
elif scale == "F":
    converted = (value - 32) * 5/9
    print(f"{value}°F is equal to {converted:.2f}°C")
else:
    print("Invalid input! Please end with C or F.")
