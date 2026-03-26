#get our little things together
import random
import signature


operators = ["+", "-", "/", "*","**"]
running = True

while running:
    user_correct = False
    selected_operator = ""
    guessed_number = 0 

    #need to create user input
    user_number = int(input("Please input the first number for ur calculation:\n"))
    user_operator = str(input(f"What type of operator do you need?\n{operators}\n(Add,Subtract,Divide,Multiply,To The Power of)\n"))
    user_number_2 = input("The second number please?: \n")
    user_guess = int(input("Now, what number do you think will come out?\n Be honest!\n"))
    # all input has been grabbed


    #convert the user input
    if user_operator == operators[0] or user_operator == "add" or user_operator == "Add" or user_operator == "ADD":
        selected_operator = "+"
    if user_operator == operators[1] or user_operator == "Subtract" or user_operator == "Sub" or user_operator == "subtract" or user_operator == "sub":
        selected_operator = "-"
    if user_operator == operators[2] or user_operator == "divide" or user_operator == "Divide":
        selected_operator = "/"
    if user_operator == operators[3] or user_operator == "multiply" or user_operator == "Multiply" or user_operator == "x":
        selected_operator = "*"
    if user_operator == operators[-1] or user_operator == "^" or user_operator == "To the power of":
        selected_operator = "**"
    #some fun
    if user_operator == "random":
        random_number = random.uniform(1,5)
        if random_number == 1:
            selected_operator = "+"
        if random_number == 2:
            selected_operator = "-"
        if random_number == 3:
            selected_operator = "/"
        if random_number == 4:
            selected_operator = "*"
        if random_number == 5:
            selected_operator = "**"
    print(f"You rolled!: {selected_operator}")
    
    #bring it together
    def Calculate(number1, operator, number2):
        number1 = int(number1)
        number2 = int(number2)
        operator = str(operator)
        result = 0
        
        if operator == "+":
            result = number1 + number2
        
        if operator == "-":
            result = number1 - number2
            
        if operator == "/":
            result = number1 / number2
        
        if operator == "*":
            result = number1 * number2
        
        if operator == "**":
            result = number1 ** number2
        
        return result
    
    
    guessed_number = user_guess
    answer = int(Calculate(user_number,selected_operator,user_number_2))
    if guessed_number == answer:
        print("Wow great job you guessed correctly! The answer is\n", answer)
        user_correct = True

    if guessed_number != answer:
        print("Yikes! Numbers are hard sometimes.\nThe answer is:",answer)
    
    user_continue = str(input("Got another calculation?\nYes or No?:"))
    user_continue = user_continue.upper()

    if (user_continue == "Yes" or user_continue == "Y"):
        print(f"So far you've got, {UserScore} correct.")
        
        
    if (user_continue == "Yes" or user_continue == "Y") and user_correct == True:
        UserScore =+ 1
        print(f"So far you've got, {UserScore} correct.")
        
        
    if (user_continue == "No" or user_continue == "N"):
        print("Thanks for playing! Hope to see you soon\n")
        running = False    
        

print(signature.about_me)

    
    
    
    
    
