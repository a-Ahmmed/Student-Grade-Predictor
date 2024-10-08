from src.regression import linearRegression

def main():
    choice = input("Choose mode; Analysis or Grade Prediction (A/GP): ").lower()
    while choice != "a" and choice != "gp":
        choice = input("Choose mode; Analysis or Grade Prediction (A/GP): ").lower()

    if choice == "a":
        print("To be implemented.\nExiting...")
    else:
        userInput = []
        questions = ["Enter Semester 1 grade: ", "Enter Semester 2 grade: ", "Enter Study Time (hours): ", "Enter No. of Failures: ", "Enter No. of Absences: "]
    
        for q in questions:
            userInput.append(input(q))
        print()
        
        try:
            inputData = [int(x) for x in userInput]
            print(linearRegression(inputData))
        except ValueError:
            print('Only Numbers should be inputted.\nExiting...')

if __name__ == "__main__":
    main()