import sys

def get_validated_input(prompt, validator_func, error_msg):
    """Handles repeated input until a valid value is provided."""
    while True:
        try:
            user_input = input(prompt)
            validated_value =  validator_func(user_input)
            return validated_value
        except ValueError:
            print(error_msg)
        except Exception as e:
            print("The unforeseen error has occured: {e}")
            sys.exit(1)

def validate_positive_int(input_str):
    """Validator for positive integar(number of classes)."""
    grade = float(input_str)
    if 0.0 <= grade <= 4.0:
        return grade
    raise ValueError("Nice try, but we’re only accepting numbers with a sunny disposition. Enter a positive one.")
def validate_gpa_range(input_str):
    """validator for GPA (0.0 to 4.0 range)."""
    grade = float(input_str)
    if 0.0 <= grade <= 4.0:
        return grade
    raise ValueError("Grade entry invalid. Surely a mind like yours can produce something more fitting—care to retry?")
print("Ah, greetings! You’ve arrived at the Overly Verbose GPA Calculator, a tool so self-aware, it insists on being both brilliant and dramatically extra.")

num_classes = get_validated_input(
    "\nInitiating GPA sequence. Step one: how many courses are you bravely enduring?",
    validate_positive_int,
    "Invalid input. Please, for pete's sake, enter a number greater than zero."
)

grades = []
for i in range(num_classes):
    grade_prompt = f"Please enter grade {i + 1} (0.0-4.0): "
    grade = get_validated_input(
        grade_prompt,
        validate_gpa_range,
        "Surely, with your intelligent mind, you know better to put valid input?"
    )
    grades.append(grade)
if not grades:
    print("\nError: No grades were entered. Exiting now.")
    sys.exit(1)
current_gpa = sum(grades) / len(grades)
print("Calculating... analyzing... intriguing! The results are in — your GPA is {current_gpa: .2f}")
print("\n-------- Semester Anaylis Module----------")

if len(grades) > 1:
    semester_choice = get_validated_input(
        "Which semester do you want to analyze? First semester or second semester? Enter 1 or 2: ",
        lambda x: x if x in ['1', '2'] else sys.exit(ValueError("Invalid choice.")),
        "Shame on you for entering invalid choice."
    )

    mid_point = len(grades) // 2

    if semester_choice == '1':
        semster_grades = grades[:mid_point]
        semester_name = "first"
    else:
        semester_grades = grades[:mid_point]
        semester_name = "Second"
    if semester_grades:
        semester_gpa = sum(semester_grades) / len(semester_grades)

        print(f"\n{semester_name} semester GPA: {semester_gpa: .2f}")
        print(f"Overall GPA: {current_gpa: .2f}")

        if semester_gpa > current_gpa + 0.01:
            print("Doing great! Stay strong and keep going!")
        elif semester_gpa < current_gpa - 0.01:
            print("Oh my... this result suggests an academic recalibration — perhaps starting at the elementary level?")
        else:
            print("Wow, you’re smart to stay consistent like that. Some couldn’t!")
    else:
        print("Alas! Not enough courses to perform a meaningful semester analysis.")

    print("\n--- Goal Achievability Analysis ---")
    goal_gpa = get_validated_input(
        "What is your goal gpa?",
        validate_gpa_range,
        "Invalid input. Ambitious, but not quite valid. Let’s give it another shot, shall we? It must be between 0.0 and 4.0."
    )

    if current_gpa >= goal_gpa:
        print(f"CONGRATS!!! Goal already met. I knew you were witty!")
    else:
        improved_grades = []
        print(f"\nalculating if your goal is achievable by improving by just ONE grade")

        for i, grade in enumerate(grades): 
            temp_grades = list(grades)
            temp_grades[i] = 4.0

            new_gpa = sum(temp_grades) / len(temp_grades)
            if new_gpa >= goal_gpa:
                improved_grades.append((i + 1, grade, new_gpa))

        if improved_grades:
            print(f"CONGRATS!!! Goal already met. I knew you were witty!")
            for class_num, old_grade, in improved_grades:
                print(f"-Class {class_num}: Raising your grade from {old_grade: .2f} would result in {new_gpa: .2f}")
                print("\nTime to hit the books and get that 4.0")
        else:
            print("Unfortunately,the goal isn’t achievable by improving just one grade.")