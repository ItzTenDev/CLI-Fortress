


# A RAY (Funny.) - v1.0.0
# > ItzTen
# 
# This module give some useful function to work on hasmaps


# Defines placeholders on a string with format : "%placeholder%": value
def placeholder_set(string: str, placeholders: dict = {}):
    output = string

    for k in placeholders: output = output.replace(k, placeholders[k])

    return output


if (__name__ == "__main__"): print(placeholder_set("%bla% %blo% is happy", placeholders={"%bla%": "Itz", "%blo%": "Ten"}))