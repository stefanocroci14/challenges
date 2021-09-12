

from roman_number import *


def check_information_structure_first_setting(str_entered, all_values_settings_mapped_dict):
    """ This function checks the structural consistency of the entered string """
    roman_numbers_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    # Conversion from string to list, using (space) separator
    lst_entered = str_entered.split(" ")
    # Check of the structural consistency of the entered string
    if len(lst_entered) != 3:
        return False
    if lst_entered[1] == "is" and lst_entered[2] in roman_numbers_dict:
        # Positive outcome of the check: storage of information
        all_values_settings_mapped_dict[lst_entered[0]] = lst_entered[2]
        return True
    else:
        return False


def check_information_structure_second_setting(str_entered, roman_numbers_allowed_symbols_list,
                                               all_values_settings_mapped_dict, multipliers_value):
    """ This function checks the structural consistency of the entered string """
    # Conversion from string to list, using (space) separator
    lst_entered = str_entered.split(" ")
    # Check of the structural consistency of the entered string
    if len(lst_entered) != 6:
        return False
    if lst_entered[0] in all_values_settings_mapped_dict and lst_entered[1] in all_values_settings_mapped_dict and \
            lst_entered[2] not in multipliers_value and lst_entered[3] == "is" and \
            lst_entered[4].isdigit() and lst_entered[5] == "Credits":
        # Positive outcome of the check: roman number generation
        roman_num = all_values_settings_mapped_dict[lst_entered[0]] + all_values_settings_mapped_dict[lst_entered[1]]
        # Check of the structural consistency of the roman number
        if check_roman_number_correct_form(roman_num, roman_numbers_allowed_symbols_list):
            # Positive outcome of the check: storage of the multiply value
            multipliers_value[lst_entered[2]] = int(lst_entered[4]) / from_roman_number_to_integer(roman_num)
            return True
        else:
            return False
    else:
        return False
