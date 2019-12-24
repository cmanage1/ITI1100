s = ''' In 1815, M. Charles-François-Bienvenu Myriel was a bishop in Digne. He was
 a seventy five years old man; he held that position in Digne since 1806. … '''

nS=s
#a
nS = nS.replace('.', ' ')
nS = nS.replace(',', ' ')
nS = nS.replace(';', ' ')
nS = nS.replace('\n', '')
print("a)", nS)

#b
nS = nS.strip()
print("b)", nS)

#c
nS = nS.lower()
print("c)", nS)

#d
print("d)", nS.count('in'))

#e
nS = nS.replace('was','is')
print("e)", nS)
