import re

def extract_steps_from_text(text):

    steps = []

    # allowed UI action keywords
    actions = ["Click", "Drag", "Open", "Select", "Enter", "Choose"]

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # check if line starts with number
        if re.match(r"^\d+", line):

            # check if action keyword exists
            for action in actions:
                if action.lower() in line.lower():
                    steps.append(line)
                    break

    return steps