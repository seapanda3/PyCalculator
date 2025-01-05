def main():
    print("""
          Welcome to pyCalculator!
          
          What operation do you want to perform?
          Enter 'a' for ADD? 's' for SUBTRACT? 'm' for MULTIPLY? 'd' for DIVIDE?
          
          
          """)
    
    while True:
        
        userInput = ''
        while userInput not in ['a', 'add', 's', 'subtract', 'm', 'multiply', 'd', 'divide']:
            print("Enter opertion to perform: ")
            userInput = input("Enter: ").lower()
        
        num1 = ''
        num2 = ''
        while not num1.isdecimal():
            print("Input should be valid!")
            num1 = input("Enter the first number: ")
        while not num2.isdecimal():
            print("Input should be valid!")
            num2 = input("Enter the last number: ")
            
        num1 = int(num1)
        num2 = int(num2)
        
        if userInput == "a" or  userInput == "add":
            result = add(num1, num2)
            print("The addition of both numbers is {}.".format(result))
                
        elif userInput == "s" or userInput == "subtract":
            result = subtract(num1, num2)
            print("The subtraction of both numbers is {}.".format(result))
            
        elif userInput == "m" or  userInput == "multiply":
            result = multiply(num1, num2)
            print("The multiplication of both numbers is {}.".format(result))
            
        elif userInput == "d" or userInput == "divide":
            result = divide(num1, num2)
            print(result)
            
        print("Do you want to perform another operation? (yes/no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Goodbye!")
    

def add(num1, num2):  
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed!"
    div = num1 / num2
    round_div = round(div, 2)
    return "The division of both numbers is {}.".format(round_div)


if __name__ == ("__main__"):
    main()