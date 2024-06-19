def getWeight():
    weight = float(input("Please enter your weight in kg: "))
    return weight

def getHeight():
    height = input("Please enter your height in feet and inches (e.g. 5'11): ")
    splitString = height.split("'")
    feet = float(splitString[0])
    inches = float(splitString[1].strip('"'))
    total_inches = (feet * 12) + inches
    return total_inches

def calculateBMI(weight, height):
    # Convert height (inches) to meters
    meterHeight = height * 0.0254
    # Calculate BMI
    bmi = weight / (meterHeight ** 2)
    return bmi

if __name__ == "__main__":
    print(" Welcome to Manpreet's BMI Calculator ! ")

    weight = getWeight()
    height = getHeight()

    bmi = calculateBMI(weight, height)
    print(f"Your final BMI is: {round(bmi, 2)}")
    if bmi < 18.5:
        print("You are underweight!")
    elif 18.5 <= bmi < 24.9:
        print("You are normal weight.")
    elif bmi >= 25:
        print("You are overweight!")
