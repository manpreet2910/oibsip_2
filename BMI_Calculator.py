def Weight_input():
    weight = float(input("Please enter your weight in kg: "))
    return weight

def Height_input():
    height = input("Please enter your height in feet and inches (e.g. 5'11): ")
    split_string = height.split("'")
    feet = float(split_string[0])
    inches = float(split_string[1].strip('"'))
    total_inches = (feet * 12) + inches
    return total_inches

def calculate_BMI(weight, height):
    meter_height = height * 0.0254
    bmi = weight / (meter_height ** 2)
    return bmi

if __name__ == "__main__":
    print(" Welcome to Manpreet's BMI Calculator ! ")

    weight = Weight_input()
    height = Height_input()

    bmi = calculate_BMI(weight, height)
    print(f"Your final BMI is: {round(bmi, 2)}")
    if bmi < 18.5:
        print("You are underweight !")
    elif 18.5 <= bmi < 24.9:
        print("You are Fit !")
    elif bmi >= 25:
        print("You are overweight!")
