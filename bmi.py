def calculate_bmi(height, weight):
   print("Height = " + str(height))
   print("Weight = " + str(weight))
   bmi= weight/(height*height)
   print("BMI = "+ f"{bmi:.2f}")
   if bmi > 25.0:
      print("Over Weight")
   elif bmi >= 18.5 or bmi<=25.0:
      print("Normal Weight")
   else:
      print("Under Weight")
calculate_bmi(weight=57, height=1.73)