import pandas as pd

# Load the NATO phonetic alphabet data from a CSV file
alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary that maps each letter to its phonetic code using iterrows
dictionary_alphabet = {row.letter: row.code for index, row in alphabet.iterrows()}

# Start the loop to get user input
found = True
while found:
    # Ask the user for input and convert it to uppercase
    user_input = input("Enter the word: ").upper()

    try:
        # Create a list of phonetic codes corresponding to the letters in the input
        new_dictionary = [dictionary_alphabet[letter] for letter in user_input]

        # Print the resulting phonetic codes list
        print(new_dictionary)

        # Exit the loop after successful input
        found = False
    except KeyError as error_message:
        # If a non-alphabet character is entered, print an error message
        print(f"Sorry, you should enter only letters. The input '{error_message}' was not found in the dictionary.")
