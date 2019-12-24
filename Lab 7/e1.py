def histogram(text):
    letters= {}

    for i in text:
        letters[i]= letters.get(i, 0) + 1

    letters = list(letters.items())
    letters.sort()
    return dict(letters)

raw_input=input("Please enter a character chain: ")

print(histogram(raw_input))
