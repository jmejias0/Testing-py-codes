name = input("What is your name? ")     # Receiving input from the user and storing it in the variable 'name'
print("Hello " + name + "!")           # String concatenation


birth_year = input("What year did you born? ")  # Here you receive a string
age = 2026 - int(birth_year)        # If we want to do the math we need to convert the string to an integer
print("You are " + str(age) + " years old.")                          # print the age to the console
