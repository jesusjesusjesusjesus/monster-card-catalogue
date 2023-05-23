easygui.msgbox("Hi there, welcome to the monster card catalogue", "Welcome", "Continue")
while not made_decision:
    usr_main_choice = easygui.buttonbox("Which action would you like to preform?", "Option select", usr_main_opts)
    if usr_main_choice == "Add a new card to the catalogue":
        usr_main_choice_int = 1
    if usr_main_choice == "Search the catalogue":
        usr_main_choice_int = 2
    if usr_main_choice == "Delete a card":
        usr_main_choice_int = 3
    if usr_main_choice == "Print all cards":
        usr_main_choice_int = 4
    made_decision = easygui.boolbox(f"you have chose {usr_main_choice}, is this correct?")


while code_run == True:
    if 0 < usr_main_choice < 5 :
        while not made_decision:
            usr_main_choice = easygui.buttonbox("Which action would you like to preform?", "Option select",
                                                usr_main_opts)
            if usr_main_choice == "Add a new card to the catalogue":
                usr_main_choice_int = 1
            if usr_main_choice == "Search the catalogue":
                usr_main_choice_int = 2
            if usr_main_choice == "Delete a card":
                usr_main_choice_int = 3
            if usr_main_choice == "Print all cards":
                usr_main_choice_int = 4
            made_decision = easygui.boolbox(f"you have chose {usr_main_choice}, is this correct?")
    # Relevent code
    usr_main_choice == 0
