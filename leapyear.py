import sys

def checkLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 
        
if __name__ == "__main__":
    y = int(sys.argv[1]) 
    
    if checkLeapYear(y):
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")    
    
    print("File name is ", sys.argv[0])

   