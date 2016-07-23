
def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    #Initialize an empty dictionary
    letter_counts = {}

    #Iterate through argument phrase, adding key, value pair to letter_counts
    for letter in phrase:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    #Initialize empty list
    most_common_letters = [0]
    
    
    #Create a for loop to iterate through values in dictionary
    for value in letter_counts.values():
    #If statement that appends to list if value is less than or equal to 
    #type in common
        if  value >= most_common_letters[0]:
            most_common_letters.append(value)
            most_common_letters.sort(reverse=True)

    #return key(s) of highest value

    return most_common_letters



print top_chars("This is my phrase")


