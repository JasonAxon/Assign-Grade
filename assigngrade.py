#criteria section
def assign_grade(score):
        if score < 0 or score > 100:
            print("Invalid score! Please enter a value between 0 and 100.")
        elif score < 60:
            print("Grade: F")
        elif score <= 69:
            print("Grade: D")
        elif score <= 79:
            print("Grade: C")
        elif score <= 89:
            print("Grade: B")
        else:
            print("Grade: A")

#input section
def inp():
     response = float(input("Please enter your grade: >> ")) # 'float' to enable numbers with decimal.
     assign_grade(response)

#start
inp()

#loop section
while True:
    contq = input("Still got any score you want to check? Y/N >> ")
    if contq == "Y":
        inp()
    else:
        print("Ok, bye.")
        break