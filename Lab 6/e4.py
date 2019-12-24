def count_v1(chain, c):
    count = 0
    for i in chain:
        if i == c:
            count += 1
    return count

def count_v2(chain, c):
    num= chain.count(c)
    return num

raw_input= input("Enter a character chain and press enter: ").strip()

print(count_v1(raw_input, 'a'))
print(count_v2(raw_input, 'a'))
