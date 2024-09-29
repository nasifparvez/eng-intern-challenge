import argparse

braille_letters = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", " ": "......"
}

braille_numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

braille_number_indicator = ".O.OOO"
braille_capital_indicator = ".....O"

def english_to_braille(message):
    output = ""
    for char in message:
        if char.isupper():
            output += braille_capital_indicator
            char = char.lower()  
        if char.isdigit():
            output += braille_number_indicator
            output += braille_numbers[char] 
        elif char in braille_letters:
            output += braille_letters[char] 
        else:
            output += braille_letters[" "] 
    return output

def braille_to_english(message):
    output = "" 
    char_is_num = False
    char_is_capital = False

    for i in range(0, len(message), 6):
        char = message[i:i+6]
        if char == braille_number_indicator:
            char_is_num = True
            continue
        if char == braille_capital_indicator:
            char_is_capital = True
            continue
        if char == braille_letters[" "]:
            char_is_num = False 
            output += " "
            continue
        if char_is_num:
            for key, val in braille_numbers.items():
                if val == char:
                    output += key
                    break
        else: 
            for key, val in braille_letters.items():
                if val == char:
                    if char_is_capital:
                        output += key.upper()
                        char_is_capital = False  
                    else:
                        output += key
                    break

    return output


def is_braille(message):
    return len(message) % 6 == 0 and all(char in "O." for char in message)

def translate(message):
    if is_braille(message):
        return braille_to_english(message)
    else:
        return english_to_braille(message)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()
    translated_text = translate(args.text)
    print(translated_text)

if __name__ == "__main__":
    main()