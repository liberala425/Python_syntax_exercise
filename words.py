def print_upper_words(words_list, must_start_with):
    """
    This function print out the words in words_list to
    upper case for those words starting with the characters
    in must_start_with set.

    words_list: a list of words
    must_start_with: a set of characters to filter the output only starting with specified characters
    """

    for w in words_list:
        if w[0] in must_start_with:
            print(w.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})