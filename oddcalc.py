number1 = input("Give me a number: ")
number2 = input("Give me another number: ")
operator = input("Give me a operator(mul/div/mod): ")

if operator == 'mul':
    number = float(number1)*float(number2)
    print(number)
elif operator == 'div':
    number = float(number1)/float(number2)
    print(number)
elif operator == 'mod':
    number = float(number1)%float(number2)
    print(number)
else:
    print("No entiendo")
