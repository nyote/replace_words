
file_names = open("../Mail Merge Project Start/Input/Names/invited_names.txt")
list_names = file_names.readlines()
# file_names.close()

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as txt:
    list_first_letter = txt.read()

    for name in list_names:
        print(name)
        new_name = name.strip()
        new_letter = list_first_letter.replace("[name]", name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as new_letters:
            new_letters.write(new_letter)

# txt.close()
# with open("starting_letter.txt", mode="w") as file:
#     file.write("")
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp