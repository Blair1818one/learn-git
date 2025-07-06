def temperature_check(temp):
    if temp > 30:
        return "Hot"
    elif temp < 10:
        return "Cold"
    else:
        return "Moderate"
    
def main():
    temp = float(input("Enter the temperature: "))
    print(f"The weather is: {temperature_check(temp)}.")

if __name__ == "__main__":
    main()

