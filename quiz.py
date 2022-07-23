print("Wellcome to Lígia's quiz!")

Name = str(input("What's your name? "))
while len(Name) <3:
    Name = str(input("What's your name? (with 3 letters or more): "))

Age = int(input("What's your age? "))
while Age < 0 or Age > 150:
    Age = int(input("Wrong age. Type again: "))

Salary = int(input("What's your salary? R$"))
while Salary < 0:
    Age = int(input("Type a value greater than 0: "))

Gender = input("What's your gender? Use M or F: ")
Gender = Gender.upper()
while Gender != "M" and Gender != "F":
    Gender = input("Type M or F: ")

Marital_Status = input("What's your marital status? Use S, M, D or W: ")
Marital_Status = Marital_Status.upper()
while Marital_Status != "S" and Marital_Status != "M" and Marital_Status != "D" and Marital_Status != "W":
    Marital_Status = input("Type S, M, D or W.")

print("You have completed the quiz. Thank you for the answers!")
