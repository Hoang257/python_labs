n = 'thisisabracadabraHt1eadljjl12ojh'
alp = ''
# uppers = [n for n in n if n.isupper()]
for i in n:
    if i == n.isupper():
        alp += i


# alp = ''.join(uppers)
pos = n.index(alp)
print(pos, alp)-------