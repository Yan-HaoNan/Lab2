def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #Code to Calculate bmi
    bmi = weight/height**2
    #Code to print BMI
    print(f"BMI = {bmi:.2f}")

    if bmi<18.5:
        print("You are Underweight")
        return -1
    elif bmi<=25:
        print("You are Normalweight")
        return 0
    else:
        print("You are Overweight")
        return 1


result = calculate_bmi(weight =57, height =1.73)