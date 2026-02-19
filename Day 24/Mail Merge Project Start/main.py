#TODO: Create a letter using starting_letter.txt

with open ("./Input./Letters./starting_letter.txt", "r") as text:
    letter = text.read()

with open ("./Input./Names./invited_names.txt") as list_of_names:
    names = list_of_names.readlines()

list_of_new_names = []

for name in names:
    new_name = name.strip()
    list_of_new_names.append(new_name)

# for each name in invited_names.txt create letter
for name in list_of_new_names:
    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output./ReadyToSend./{name}.txt","w") as inviting:
        # Replace the [name] placeholder with the actual name.
        new_letter = letter.replace("[name]", f"{name}")
        inviting.write(new_letter)

    #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp