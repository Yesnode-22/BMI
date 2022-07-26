#Body Mass Index(BMI) caculator
height = input("enter your height in m:")
weight = input("enter your weight in Kg:")
bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)
new_bmi_as_int = str(bmi_as_int)
print("Your BMI is " + "" + new_bmi_as_int)