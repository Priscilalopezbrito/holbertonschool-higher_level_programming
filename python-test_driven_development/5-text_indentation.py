#!/usr/bin/python3
"""
Module contains function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines

    Parameters:
        text (str): Text string
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = ""
    i = 0
    while i < len(text):
        new += text[i]
        if text[i] in ['.', '?', ':']:
            new += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(new, end="")
