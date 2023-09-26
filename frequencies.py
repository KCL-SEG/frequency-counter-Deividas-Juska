"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items :
        if isinstance(i, str):
            if (i in frequencies):
                frequencies[i] += 1
            else:
                frequencies[i] = 1
        else:
            i = str(i)
            if (i in frequencies):
                frequencies[i] += 1
            else:
                frequencies[i] = 1

    return frequencies
