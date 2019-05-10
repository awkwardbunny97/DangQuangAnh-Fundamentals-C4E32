height = int(input('Input your height (cm) : '))
weight = int(input('Input your weight (kg) : '))
meter = height * 0.01
BMI = weight / ( meter*meter )

if BMI < 16:
    print('Severely underweight')
elif 16 < BMI < 18.5:
    print('Underweight')
elif 18.5 < BMI < 25:
    print('Normal')
elif 25 < BMI < 30:
    print('Overweight')
else:
    print('Obese')