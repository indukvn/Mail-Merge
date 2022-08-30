lst = []
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    invited_name = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as ltr_file:
    starting_ltr = ltr_file.read()
    for name in invited_name:
        new_name = name.strip()
        new_ltr = starting_ltr.replace(PLACEHOLDER, new_name)

        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as final_ltr:
            final_ltr.write(new_ltr)




