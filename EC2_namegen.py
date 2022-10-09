import random
import string
import sys

def string_generator (size=8, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))
    
department = input("Enter Department: Marketing, Accounting, FinOps: ")

for _ in department:
    if department == "Marketing" or department.lower() == "marketing" :
        print("Processing... ")
        break
    elif department == "Accounting" or department.lower() == "accounting" :
        print("Processing... ")
        break
    elif department == "FinOps" or department.lower() == "finops" :
        print("Processing... ")
        break
    else:
        print("Error: You are not authorized to use this name generator. Please enter appropriate department. ")
        raise SystemExit
        
number = int(input("Enter amount of EC2 instances: "))

if number < 1:
    print("Please enter number greater than 0 ")
elif number > 0:
    print("")
    
print("Generated EC2 Instances Names: ")

for _ in range(1, number + 1):
    unique_name = department
    EC2_unique_name = unique_name + "-" + string_generator()
    print("EC2 Instance's names: ", EC2_unique_name)
    