import easygui


def word_to_number(word):
    """
    Convert a word number up to twenty-five (e.g. "three") into an integer (e.g. 3).
    """
    number_words = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'twenty-one': 21,
        'twenty-two': 22,
        'twenty-three': 23,
        'twenty-four': 24,
        'twenty-five': 25
    }

    # If the word is already a number, return it as an integer
    if word.isnumeric():
        return int(word)

    # Split the word into individual words
    words = word.lower().split()

    # Handle negative numbers
    if words[0] == 'minus':
        return -word_to_number(' '.join(words[1:]))

    # Convert the word number into an integer
    number = 0
    for word in words:
        if word in number_words:
            number += number_words[word]
        else:
            raise ValueError(f"Invalid word number: {word}")

    # Check if the number is greater than 25
    if number > 25:
        raise ValueError("Number must be 25 or less.")

    return number


monsters = {
    1: {"ID": 1, "name": "Stoneling", "strength": 7, "speed": 1, "stealth": 25, "cunning": 15, "filled_out": "1"},
    2: {"ID": 2, "name": "Vexscream", "strength": 1, "speed": 6, "stealth": 21, "cunning": 19, "filled_out": "1"},
    3: {"ID": 3, "name": "Dawnmirage", "strength": 5, "speed": 15, "stealth": 18, "cunning": 22, "filled_out": "1"},
    4: {"ID": 4, "name": "Blazegolem", "strength": 15, "speed": 20, "stealth": 23, "cunning": 6, "filled_out": "1"},
    5: {"ID": 5, "name": "Websnake", "strength": 7, "speed": 15, "stealth": 10, "cunning": 5, "filled_out": "1"},
    6: {"ID": 6, "name": "Moldvine", "strength": 21, "speed": 18, "stealth": 14, "cunning": 5, "filled_out": "1"},
    7: {"ID": 7, "name": "Vortexwing", "strength": 19, "speed": 13, "stealth": 19, "cunning": 2, "filled_out": "1"},
    8: {"ID": 8, "name": "Rotthing", "strength": 16, "speed": 7, "stealth": 4, "cunning": 12, "filled_out": "1"},
    9: {"ID": 9, "name": "Froststep", "strength": 14, "speed": 14, "stealth": 17, "cunning": 4, "filled_out": "1"},
    10: {"ID": 10, "name": "Wispghoul", "strength": 17, "speed": 19, "stealth": 3, "cunning": 2, "filled_out": "1"},
    11: {"ID": 11, "name": "", "strength": 0, "speed": 0, "stealth": 0, "cunning": 0, "filled_out": "0"},
    12: {"ID": 12, "name": "", "strength": 0, "speed": 0, "stealth": 0, "cunning": 0, "filled_out": "0"},
    13: {"ID": 13, "name": "", "strength": 0, "speed": 0, "stealth": 0, "cunning": 0, "filled_out": "0"},
    14: {"ID": 14, "name": "", "strength": 0, "speed": 0, "stealth": 0, "cunning": 0, "filled_out": "0"},
    15: {"ID": 15, "name": "", "strength": 0, "speed": 0, "stealth": 0, "cunning": 0, "filled_out": "0"}
            }
search_func = ""
monster_names = ["Stoneling", "Vexscream", "Dawnmirage", "Blazegolem", "Websnake", "Moldvine", "Vortexwing",
                 "Rotthing", "Froststep", "Wispghoul"]
monster_attributes = ["strength", "speed", "stealth", "cunning"]
monster_name_int = 0
yes_no = ["yes", "no"]
correct_callback = ""
incorrect_attribute = ""
monster_attribute_int = 0
function_use = True


while function_use:
    easygui.msgbox("you have chosen to search the catalogue for an existing card")
    search_func = easygui.choicebox("choose a monster to review", "choose a monster", monster_names)
    monster_name_int = monster_names.index(search_func) + 1
    correct_callback = easygui.choicebox(f"{monsters[monster_name_int]['name']}:"
                                         f"\nStrength: {monsters[monster_name_int]['strength']}"
                                         f"\nSpeed: {monsters[monster_name_int]['speed']}\n"
                                         f"Stealth: {monsters[monster_name_int]['stealth']}"
                                         f"\nCunning: {monsters[monster_name_int]['cunning']}\n\n"
                                         f"Do you want to make any changes?", "Selected Card", yes_no)
    if correct_callback == "yes":
        while correct_callback == "yes":
            incorrect_attribute = easygui.choicebox(f"which attribute is wrong\n {monsters[monster_name_int]['name']}"
                                                    f"\nStrength: {monsters[monster_name_int]['strength']}"
                                                    f"\nSpeed: {monsters[monster_name_int]['speed']}\n"
                                                    f"Stealth: {monsters[monster_name_int]['stealth']}"
                                                    f"\nCunning: {monsters[monster_name_int]['cunning']},", "attributes",
                                                    monster_attributes)
            monster_attribute_int = monster_attributes.index(incorrect_attribute)
            print(monster_attribute_int)
            monsters[monster_name_int][monster_attributes[monster_attribute_int]] = \
                easygui.integerbox(
                    f"{monster_attributes[monster_attribute_int]} for "
                    f"{monsters[monster_name_int]['name']}: enter desired value",
                    "correcting attribute", 0, 1, 25)
            correct_callback = easygui.choicebox(f"{monsters[monster_name_int]['name']}"
                                                 f"\nStrength: {monsters[monster_name_int]['strength']}"
                                                 f"\nSpeed: {monsters[monster_name_int]['speed']}\n"
                                                 f"Stealth: {monsters[monster_name_int]['stealth']}"
                                                 f"\nCunning: {monsters[monster_name_int]['cunning']}\n\n"
                                                 f"Do you want to make any changes?", "Selected Card", yes_no)
            print(monsters)
    if correct_callback == "no":
        function_use = False
