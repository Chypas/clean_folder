#!/usr/bin/python
# -*- coding: utf8 -*-

import re


def normalize(string):
    capital_letters = {
        u"А": u"A",
        u"Б": u"B",
        u"В": u"V",
        u"Г": u"G",
        u"Ґ": u"G",
        u"Д": u"D",
        u"Е": u"E",
        u"Є": u"E",
        u"Ж": u"Zh",
        u"З": u"Z",
        u"И": u"U",
        u"І": u"I",
        u"Й": u"Y",
        u"К": u"K",
        u"Л": u"L",
        u"М": u"M",
        u"Н": u"N",
        u"О": u"O",
        u"П": u"P",
        u"Р": u"R",
        u"С": u"S",
        u"Т": u"T",
        u"У": u"U",
        u"Ф": u"F",
        u"Х": u"H",
        u"Ц": u"Ts",
        u"Ч": u"Ch",
        u"Ш": u"Sh",
        u"Щ": u"Sch",
        u"Ь": u"I",
        u"Ю": u"Yu",
        u"Я": u"Ya"
    }
    lower_case_letters = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"ґ": u"g",
        u"д": u"d",
        u"е": u"e",
        u"є": u"e",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"u",
        u"і": u"i",
        u"ї": u"y",
        u"й": u"y",
        u"к": u"k",
        u"л": u"l",
        u"м": u"m",
        u"н": u"n",
        u"о": u"o",
        u"п": u"p",
        u"р": u"r",
        u"с": u"s",
        u"т": u"t",
        u"у": u"u",
        u"ф": u"f",
        u"х": u"h",
        u"ц": u"ts",
        u"ч": u"ch",
        u"ш": u"sh",
        u"щ": u"sch",
        u"ь": u"i",
        u"ю": u"yu",
        u"я": u"ya"
    }

    normalize_string = ""
    for index, char in enumerate(string):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(string) > index+1:
                if string[index+1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        if not re.search("[a-z A-Z0-9.]", char):
            char = "-"
        normalize_string += char
    return normalize_string
