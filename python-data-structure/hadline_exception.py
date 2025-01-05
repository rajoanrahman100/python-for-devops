
try: # General exception
    age=int(input("Age: "))
    income=50000
    risk=income/age
    print(f"Risk: {risk:.3f}") # 3 decimal places
    
except ZeroDivisionError: # Specific exception
    print("Age cannot be zero")    

except ValueError: # Specific exception
    print("Invalid value")