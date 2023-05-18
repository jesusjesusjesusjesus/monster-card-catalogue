import easygui


def __init__(self, msg, title, fields, values, mask_last=False, **kwargs):
    self.fields, self.values = self.check_fields(fields, values)
    if self.fields is None:
        self.fields = []
    if self.values is None:
        self.values = []


def word_to_number(word):
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
    if word.isnumeric():
        return int(word)
    words = word.lower().split()
    if words[0] == 'minus':
        return -word_to_number(' '.join(words[1:]))
    number = 0
    for word in words:
        if word in number_words:
            number += number_words[word]
        else:
            raise ValueError(f"Invalid word number: {word}")
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
valid_numbers = []
usr_func1_chcs = ["Yes", "No"]
numbers_int = ["", 0, 0, 0, 0]
numbers_str = ["", "", "", "", ""]
card_fields = ["name", "strength", "speed", "stealth", "cunning"]
card_filled = False
correct_cmpt = True
frst_emty_enty = 0
monster_attributes = ["name", "strength", "speed", "stealth", "cunning"]
crd_crrt = True

usr_sure = easygui.buttonbox(f"in this section you can add your card to the existing deck\n\n"
                             f"are you sure you want to continue?\n", "Function description", usr_func1_chcs)
while correct_cmpt:
    if usr_sure == "Yes":
        while not card_filled:
            numbers_str = easygui.multenterbox("write the desired stats in the appropriate fields below, "
                                               "numbers will not work", "New monster card", card_fields, valid_numbers)
            numbers_str = [value if value is not None else "" for value in numbers_str]
            for i in range(len(numbers_str)):
                if not bool(numbers_str[i]):
                    if numbers_str[i] != "":
                        numbers_int[numbers_int[i]] = numbers_str
                        valid_numbers.append(numbers_str)
                    numbers_str = easygui.multenterbox("You have left a blank space.\n"
                                                       "Write the desired stats in the appropriate fields below.\n"
                                                       "Numbers will not work.", "New monster card", card_fields,
                                                       valid_numbers)
            card_filled = True
        else:
            numbers_int[numbers_int[i]] = word_to_number(numbers_str[i])
        for key in monsters:
            if monsters[key]["filled_out"] == "0":
                frst_emty_enty = key
                break
        for i, attr in enumerate(monster_attributes):
            value = numbers_str[i]
            monsters[frst_emty_enty][attr] = value
        monsters[frst_emty_enty]['filled_out'] = 1
        crd_crrt = easygui.boolbox(f"are the following details correct?\n\n"
                                   f"{monsters[frst_emty_enty]}", "card correct?")
        if not crd_crrt:
            while not crd_crrt:
                incorrect_attribute = easygui.choicebox(f"which attribute is wrong\n {monsters[frst_emty_enty]['name']}"
                                                        f"\nStrength: {monsters[frst_emty_enty]['strength']}"
                                                        f"\nSpeed: {monsters[frst_emty_enty]['speed']}\n"
                                                        f"Stealth: {monsters[frst_emty_enty]['stealth']}"
                                                        f"\nCunning: {monsters[frst_emty_enty]['cunning']},",
                                                        "attributes", monster_attributes[1:5])
                monster_attribute_int = monster_attributes.index(incorrect_attribute)
                print(monster_attribute_int)
                monsters[frst_emty_enty][monster_attributes[monster_attribute_int]] = \
                    easygui.integerbox(
                        f"{monster_attributes[monster_attribute_int]} for "
                        f"{monsters[frst_emty_enty]['name']}: enter desired value",
                        "correcting attribute", 0, 1, 25)
                correct_callback = easygui.choicebox(f"{monsters[frst_emty_enty]['name']}"
                                                     f"\nStrength: {monsters[frst_emty_enty]['strength']}"
                                                     f"\nSpeed: {monsters[frst_emty_enty]['speed']}\n"
                                                     f"Stealth: {monsters[frst_emty_enty]['stealth']}"
                                                     f"\nCunning: {monsters[frst_emty_enty]['cunning']}\n\n"
                                                     f"Do you want to make any changes?", "Selected Card",
                                                     usr_func1_chcs)
                crd_crrt = easygui.boolbox(f"are the following details correct?\n\n"
                                           f"{monsters[frst_emty_enty]}", "card correct?")
        if crd_crrt:
            break
            # back to the home screen
        card_filled = True
    if usr_sure == "No":
        correct_cmpt = False
        # back to the home screen
