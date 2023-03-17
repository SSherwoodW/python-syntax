def print_upper_words(words):
    """Print each word on a separate line in uppercase
    """

    for word in words:
        print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words2(words):
    """Print each word on a separate line
        if it starts with letter E/e"""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

print_upper_words2(["Ectoplasm", "erin", "Richard", "Ernesto"])

def print_upper_words3(words, must_start_with):
    """Print each word on a separate line
        if it starts with the letters defined in must_start_with"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter) or word.startswith(letter.upper()):
                print(word.upper())

print_upper_words3(["Ectoplasm", "erin", "Richard", "Ernesto", "Chimichanga", "Orion", "ripmeanewone"],
                   ['r', 'e'])
