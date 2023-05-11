import easygui


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


valid_numbers = []
usr_func1_chcs = ("Yes", "No")
numbers_int = ["", 0, 0, 0, 0]
numbers_str = ("", "", "", "", "")
card_fields = ("name", "strength", "speed", "stealth", "cunning")
card_filled = False
correct_cmpt = True

usr_sure = easygui.buttonbox(f"in this section you can add your card to the existing deck\n\n"
                             f"are you sure you want to continue?\n", "Function description", usr_func1_chcs)
while correct_cmpt:
    if usr_sure == "Yes":
        while not card_filled:
            numbers_str = easygui.multenterbox("write the desired stats in the appropriate fields below\n"
                                               "numbers will not work", "New monster card", card_fields)



            #fix this code


            for i in range(1, len(numbers_str) + 1):
                if not bool(numbers_str[i]):
                    if numbers_str[i] != 0:
                        numbers_int[numbers_int[i]] = numbers_str
                        valid_numbers.append(numbers_str)
                    numbers_str = easygui.multenterbox("you have left a blank space\n"
                                                       "write the desired stats in the appropriate fields below\n"
                                                       "numbers will not work", "New monster card", card_fields,
                                                       valid_numbers)
else:
    numbers_int[numbers_int[i]] = word_to_number(numbers_str[i])

    if usr_sure == "No":
        correct_cmpt = False
