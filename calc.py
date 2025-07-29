a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))




# function to determine the action chose
def action():
    print('action chosen')
    print('Available operations:')
    print('* for multiplication') 
    print('+ for addition')
    print('- for subtraction')
    print('/ for division')
    print('Please enter your choice:')      

    choice = input('Enter your choice: ')
    if choice == '*':
        print('You chose multiplication')
        return a * b
    elif choice == '+':
        print('You chose addition')
        return a + b
    elif choice == '-':
        print('You chose subtraction')
        return a - b
    elif choice == '/':
        print('You chose division')
        return a / b
    else:
        print('Invalid choice, please try again')
        return action()
    
print('Result:', action())