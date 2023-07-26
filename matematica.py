import random

def generate_addition():
    num1 = random.randint(100, 5000)
    num2 = random.randint(100, 5000)
    result = num1 + num2
    return f"{num1} + {num2} = _____"

def generate_subtraction():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    num1, num2 = max(num1, num2), min(num1, num2)
    result = num1 - num2
    return f"{num1} - {num2} = _____"

def generate_multiplication():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    result = num1 * num2
    return f"{num1} x {num2} = _____"

def generate_division():
    num1 = random.randint(2, 10)
    num3 = random.randint(2, 10)
    num2 = num1 * num3
    num1, num2 = max(num1, num2), min(num1, num2)
    result = num2 // num1
    return f"{num1} ÷ {num2} = _____"

def generate_division2():
    num1 = random.randint(2, 100)
    num2 = random.randint(2, 10)
    num1, num2 = max(num1, num2), min(num1, num2)
    if num1 %2 != 0:
        num1 += 1
    if num2 %2 != 0:
        num2 += 1 
    result = num1 // num2
    return f"{num1} ÷ {num2} = _____"

def generate_division3():
    num1 = random.randint(2, 100)
    num2 = random.randint(2, 10)
    num1, num2 = max(num1, num2), min(num1, num2)
    result = num1 // num2
    return f"{num1} ÷ {num2} = _____"

def generate_exercises(operation, num_exercises):
    exercises = []
    
    if operation == "addition":
        generator = generate_addition
    elif operation == "subtraction":
        generator = generate_subtraction
    elif operation == "multiplication":
        generator = generate_multiplication
    elif operation == "division":
        generator = generate_division
    elif operation == "division2":
        generator = generate_division2
    elif operation == "division3":
        generator = generate_division3
    else:
        print("Tipo de operação inválido!")
        return exercises
    
    for _ in range(num_exercises):
        exercises.append(generator())
    
    random.shuffle(exercises)
    return exercises

operation = input("Digite o tipo de operação (addition, subtraction, multiplication, division, division2 or division3): ")
num_exercises = int(input("Digite o número de exercícios a serem gerados: "))

exercises = generate_exercises(operation, num_exercises)

for exercise in exercises:
    print(exercise)

