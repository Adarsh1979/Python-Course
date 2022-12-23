with open("../Input/Names/invited_names.txt") as file1:
    names = file1.readlines()

with open("../Input/Letters/start_letter.txt") as file2:
    letter = file2.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]", stripped_name)
        with open(f"../Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file3:
            file3.write(new_letter)

