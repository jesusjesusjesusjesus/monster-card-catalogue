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


# main dic
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
# welcome scrn var
usr_welcm_opts = ("Add a new card to the catalogue", "Search the catalogue", "Delete a card", "Print all cards",
                  "End program")
usr_welcm_choice = ""
usr_welcm_choice_int = 0
made_decision_welcm = False

# component one var
valid_numbers = []
usr_func1_chcs = ["Yes", "No"]
numbers_int = ["", 0, 0, 0, 0]
numbers_str = ["", "", "", "", ""]
card_filled = False
correct_cmpt = True
frst_emty_enty = 0
monster_attributes = ["name", "strength", "speed", "stealth", "cunning"]
crd_crrt = True

# component two var
monster_names_lst = []
monster_name_int = 0
yes_no = ["yes", "no"]
correct_callback = ""
incorrect_attribute = ""
monster_attribute_int = 0

# component three var
delete_sure = False
monster_names = []
monster_int = 0

# component four var
# all are shared with other comp var
# (see shared var)

# shared var
card_info = ""  # cmpt4, cmpt3
function_use = True  # cmpt4, cmpt2
search_func = ""  # cmpt3, cmpt2
card_fields = ["name", "strength", "speed", "stealth", "cunning"]  # cmpt3, cmpt1

# correct cmpt var
game_play = True


easygui.msgbox("Hi there, welcome to the monster card catalogue", "Welcome", "Continue")
while game_play:
    while not made_decision_welcm:
        usr_welcm_choice = easygui.buttonbox("Which action would you like to preform?", "Option select", usr_welcm_opts)
        if usr_welcm_choice == "Add a new card to the catalogue":
            usr_welcm_choice_int = 1
        if usr_welcm_choice == "Search the catalogue":
            usr_welcm_choice_int = 2
        if usr_welcm_choice == "Delete a card":
            usr_welcm_choice_int = 3
        if usr_welcm_choice == "Print all cards":
            usr_welcm_choice_int = 4
        if usr_welcm_choice == "End program":
            usr_welcm_choice_int = 5
        if usr_welcm_choice == None:
            easygui.msgbox("Please choose an action\n(if you dont want to preform any function just press "
                           "'End program'")
        if 0 < usr_welcm_choice_int < 6:
            made_decision_welcm = easygui.boolbox(f"You have chosen {usr_welcm_choice}, is this correct?")

    if usr_welcm_choice_int == 1:
        usr_sure = easygui.buttonbox(f"In this section you can add your card to the existing deck\n\n"
                                     f"are you sure you want to continue?\n", "Function description", usr_func1_chcs)
        while correct_cmpt:
            if usr_sure == "Yes":
                while not card_filled:
                    numbers_str = easygui.multenterbox(f"Write the desired stats in the appropriate fields below, "
                                                       f"PLease enter an integer\n(1-25)", "New monster card", card_fields,
                                                       valid_numbers)
                    numbers_str = [value if value is not None else "" for value in numbers_str]
                    for i in range(len(numbers_str)):
                        if not bool(numbers_str[i]):
                            if numbers_str[i] != "":
                                numbers_int[numbers_int[i]] = numbers_str
                                valid_numbers.append(numbers_str)
                            numbers_str = easygui.multenterbox("You have left a blank space.\n"
                                                               "Write the desired stats in the "
                                                               "appropriate fields below.\n"
                                                               "Please enter an integer.\n(1-25)", "New monster card",
                                                               card_fields, valid_numbers)

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
                monsters[frst_emty_enty]['filled_out'] = "1"
                print(monsters[frst_emty_enty]['filled_out'])
                crd_crrt = easygui.boolbox(f"Are the following details correct?\n\n"
                                           f"{monsters[frst_emty_enty]}", "card correct?")
                if not crd_crrt:
                    while not crd_crrt:
                        incorrect_attribute = easygui.choicebox(f"Which attribute is wrong\n "
                                                                f"{monsters[frst_emty_enty]['name']}"
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
                                f"{monsters[frst_emty_enty]['name']}: Enter desired value\n(1-25)",
                                "correcting attribute", 0, 1, 25)
                        correct_callback = easygui.choicebox(f"{monsters[frst_emty_enty]['name']}"
                                                             f"\nStrength: {monsters[frst_emty_enty]['strength']}"
                                                             f"\nSpeed: {monsters[frst_emty_enty]['speed']}\n"
                                                             f"Stealth: {monsters[frst_emty_enty]['stealth']}"
                                                             f"\nCunning: {monsters[frst_emty_enty]['cunning']}\n\n"
                                                             f"Do you want to make any changes?", "Selected Card",
                                                             usr_func1_chcs)
                        crd_crrt = easygui.boolbox(f"Are the following details correct?\n\n"
                                                   f"{monsters[frst_emty_enty]}", "card correct?")
                if crd_crrt:
                    break
                    # back to the home screen
                card_filled = True
            if usr_sure == "No":
                correct_cmpt = False
                # back to the home screen
    made_decision_welcm = False
    if usr_welcm_choice_int == 2:
        while function_use:
            for i in monsters:
                if monsters[i]["filled_out"] == "1":
                    monster_names_lst.append(monsters[i]['name'])
            easygui.msgbox("You have chosen to search the catalogue for an existing card and afterward you can decide "
                           "to edit it")
            search_func = easygui.choicebox("choose a monster to review", "choose a monster", monster_names_lst)
            monster_name_int = monster_names_lst.index(search_func) + 1
            correct_callback = easygui.choicebox(f"{monsters[monster_name_int]['name']}:"
                                                 f"\nStrength: {monsters[monster_name_int]['strength']}"
                                                 f"\nSpeed: {monsters[monster_name_int]['speed']}\n"
                                                 f"Stealth: {monsters[monster_name_int]['stealth']}"
                                                 f"\nCunning: {monsters[monster_name_int]['cunning']}\n\n"
                                                 f"Do you want to make any changes?", "Selected Card", yes_no)
            if correct_callback == "yes":
                while correct_callback == "yes":
                    incorrect_attribute = easygui.choicebox(f"Which attribute is wrong\n "
                                                            f"{monsters[monster_name_int]['name']}"
                                                            f"\nStrength: {monsters[monster_name_int]['strength']}"
                                                            f"\nSpeed: {monsters[monster_name_int]['speed']}\n"
                                                            f"Stealth: {monsters[monster_name_int]['stealth']}"
                                                            f"\nCunning: {monsters[monster_name_int]['cunning']},",
                                                            f"attributes", monster_attributes[1:5])
                    monster_attribute_int = monster_attributes.index(incorrect_attribute)
                    print(monster_attribute_int)
                    monsters[monster_name_int][monster_attributes[monster_attribute_int]] = \
                        easygui.integerbox(
                            f"{monster_attributes[monster_attribute_int]} for "
                            f"{monsters[monster_name_int]['name']}: Enter desired value\n(1-25)",
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
            made_decision_welcm = False
    if usr_welcm_choice_int == 3:
        easygui.msgbox("You have chosen to delete a card")
        for key in monsters:
            monster_names.append(monsters[key]['name'])

        search_func = easygui.choicebox("Choose a monster to delete", "choose a monster", monster_names)
        for key in monsters:
            if search_func == monsters[key]['name']:
                monster_int = key
        delete_sure = easygui.boolbox(f"Are you sure you want to delete this card?\n\n"
                                      f"name: {monsters[monster_int]['name']}\n"
                                      f"strength: {monsters[monster_int]['strength']}\n"
                                      f"speed: {monsters[monster_int]['speed']}\n"
                                      f"stealth: {monsters[monster_int]['stealth']}\n"
                                      f"cunning: {monsters[monster_int]['cunning']}", "delete card?")
        if delete_sure:
            while delete_sure:
                monsters[monster_int]['name'] = ""
                monsters[monster_int]['strength'] = 0
                monsters[monster_int]['speed'] = 0
                monsters[monster_int]['stealth'] = 0
                monsters[monster_int]['cunning'] = 0
                monsters[monster_int]['filled_out'] = 0
                for key, value in monsters.items():
                    if value.get('filled_out') == "1":
                        card_info += (
                            f"ID: {value.get('ID')}\n"
                            f"Name: {value.get('name')}\n"
                            f"Strength: {value.get('strength')}\n"
                            f"Speed: {value.get('speed')}\n"
                            f"Stealth: {value.get('stealth')}\n"
                            f"Cunning: {value.get('cunning')}\n\n"
                        )

                if card_info:
                    easygui.msgbox(card_info)
                else:
                    easygui.msgbox("No filled-out monster cards found.")
                delete_sure = False
            made_decision_welcm = False
    if usr_welcm_choice_int == 4:
        while function_use:
            easygui.msgbox("You have chosen to print all filled-out monster cards")

            for key, value in monsters.items():
                if value.get('filled_out') == "1":
                    card_info += (
                        f"ID: {value.get('ID')}\n"
                        f"Name: {value.get('name')}\n"
                        f"Strength: {value.get('strength')}\n"
                        f"Speed: {value.get('speed')}\n"
                        f"Stealth: {value.get('stealth')}\n"
                        f"Cunning: {value.get('cunning')}\n\n"
                    )

            if card_info:
                easygui.msgbox(card_info)
                print(card_info)
            else:
                easygui.msgbox("No filled-out monster cards found.")
            function_use = False
            made_decision_welcm = False
    if usr_welcm_choice_int == 5:
        easygui.msgbox("Thank you for participating")
        quit()
