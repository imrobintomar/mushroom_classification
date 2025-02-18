import inquirer


def get_user_input():
    # Define the initial question to ask the user
    initial_question = [
        inquirer.List(
            "action",
            message="What would you like to do?",
            choices=["Predict", "Exit"],
        )
    ]

    # Define the questions to ask the user for the prediction
    feature_questions = [
        inquirer.Text("cap-diameter", message="Enter cap diameter (cm)"),
        inquirer.Text("cap-shape", message="Enter cap shape (0-6)"),
        inquirer.Text("gill-attachment", message="Enter gill attachment (0-6)"),
        inquirer.Text("gill-color", message="Enter gill color (0-11)"),
        inquirer.Text("stem-height", message="Enter stem height (cm)"),
        inquirer.Text("stem-width", message="Enter stem width (cm)"),
        inquirer.Text("stem-color", message="Enter stem color (0-12)"),
        inquirer.Text(
            "season",
            message="Enter season (0 - Early Season, 1 - Late Season, 1.75 - All Season)",
        ),
    ]

    initial_answer = inquirer.prompt(initial_question)

    if initial_answer["action"] == "Predict":
        while True:
            feature_answers = inquirer.prompt(feature_questions)

            # Validate numeric inputs
            try:
                cap_diameter = float(feature_answers["cap-diameter"])
                stem_height = float(feature_answers["stem-height"])
                stem_width = float(feature_answers["stem-width"])
                season = float(feature_answers["season"])
            except ValueError:
                print(
                    "Please enter valid numeric values for cap diameter, stem height, stem width, and season."
                )
                continue

            # Validate categorical inputs
            if not (0 <= int(feature_answers["cap-shape"]) <= 6):
                print("Please enter a valid choice for cap shape (0-6).")
                continue
            if not (0 <= int(feature_answers["gill-attachment"]) <= 6):
                print("Please enter a valid choice for gill attachment (0-6).")
                continue
            if not (0 <= int(feature_answers["gill-color"]) <= 11):
                print("Please enter a valid choice for gill color (0-11).")
                continue
            if not (0 <= int(feature_answers["stem-color"]) <= 12):
                print("Please enter a valid choice for stem color (0-12).")
                continue

            # Update feature answers with validated numeric values
            feature_answers["cap-diameter"] = cap_diameter
            feature_answers["stem-height"] = stem_height
            feature_answers["stem-width"] = stem_width
            feature_answers["season"] = season

            return feature_answers
    else:
        return None
