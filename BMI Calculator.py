weight  = float(input())
height = float(input())
BMI=weight/(height*height)
if BMI < 18.5 :
    print("Underweight")
elif BMI >= 18.5  and BMI<25.5:
    print("Normal")
elif BMI >= 25.5 and BMI < 30 :
    print("Overweight")
else:
    print("Obesity")