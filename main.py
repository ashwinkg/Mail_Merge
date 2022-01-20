# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# reading the line by line from file and storing in a list
with open(file="./Input/Names/invited_names.txt", mode="r") as file:
    invited_name_list = file.readlines()

# replacing the /n with empty string
for i in range(len(invited_name_list)):
    name = invited_name_list[i].replace("\n", "")
    invited_name_list[i] = name

search_text = "[name]"

# reading from starting_letter
with open(file="./Input/Letters/starting_letter.txt", mode="r") as file:
    content = file.read()
    for name in invited_name_list:
        new_name = content.replace(search_text, name)
        with open(file=f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
            new_file.write(new_name)
