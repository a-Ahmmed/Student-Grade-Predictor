from src.regression import linearRegression

def main():
    choice = input("Choose mode; Analysis or Grade Prediction (A/GP): ").lower()
    while choice != "a" and choice != "gp":
        choice = input("Choose mode; Analysis or Grade Prediction (A/GP): ").lower()

    if choice == "a":
        print("To be implemented.\nExiting...")
    else:
        userInput = []
        userInput.append(input("Enter Semester 1 grade: "))
        userInput.append(input("Enter Semester 2 grade: "))
        userInput.append(input("Enter Study Time (hours): "))
        userInput.append(input("Enter No. of Failures: "))
        userInput.append(input("Enter No. of Absences: "))
        print()
        
        try:
            inputData = [int(x) for x in userInput]
            print(linearRegression(inputData))
        except ValueError:
            print('Only Numbers should be inputted.\nExiting...')

if __name__ == "__main__":
    main()