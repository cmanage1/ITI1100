def spaces(s):
    ch= ''
    for i in s:
        ch += i + ' '

    return (ch.strip())

raw_input= input("Enter a word: ").strip()

sprint(spaces(raw_input))
