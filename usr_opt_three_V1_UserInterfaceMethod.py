import easygui

delete_sure = False
search_func = ""
monster_names = []
card_fields = ["name", "strength", "speed", "stealth", "cunning"]
monster_int = 0
card_info = ""
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

easygui.msgbox("you have chosen to delete a card")
for key in monsters:
    monster_names.append(monsters[key]['name'])

search_func = easygui.choicebox("choose a monster to delete", "choose a monster", monster_names)
for key in monsters:
    if search_func == monsters[key]['name']:
        monster_int = key
delete_sure = easygui.boolbox(f"are you sure you want to delete this card?\n\n"
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
            easygui.textbox(card_info)
        else:
            easygui.msgbox("No filled-out monster cards found.")
    delete_sure = False
