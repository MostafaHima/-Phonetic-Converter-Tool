# Phonetic Converter Tool

## Description
Converts user-input words into NATO phonetic alphabet codes using a CSV-based dictionary, with error handling for invalid characters.

## Features
- Converts letters to NATO phonetic alphabet codes.
- Reads data from a CSV file for phonetic mappings.
- Provides error handling for non-alphabetic characters.

## How It Works
1. Loads NATO phonetic alphabet codes from a CSV file.
2. Prompts the user for input and converts it to uppercase.
3. Maps each letter of the input to its corresponding phonetic code.
4. Displays an error message if the input contains invalid characters.

## Requirements
- Python 3.6+
- pandas library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/MostafaHima/-Phonetic-Converter-Tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Phonetic-Converter-Tool
   ```
3. Install required dependencies:
   ```bash
   pip install requirements.txt
   ```

## Usage
1. Ensure the `nato_phonetic_alphabet.csv` file is in the same directory.
2. Run the script:
   ```bash
   python main.py
   ```
3. Enter a word when prompted, and the program will display the phonetic codes.

## Example
Input:
```
Enter The word: Hello
```
Output:
```
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

If invalid characters are entered:
```
Sorry, you should write only letters. This input "1" is not found in the dictionary.
```


