a = 'QWERTYUIOPASDFGHJKLZXCVBNM'
b = '012345689'
ch = 'thisisabracadabraHt1eadljjl12ojh.'
word = ''
moves = []
for i in range(len(ch)):
    if ch[i] in a:
        word += ch[i]
        moves.append(i)
        break
for i in range(len(ch)):
    if ch[i] in b:
        word += ch[i+1]
        moves.append(i+1)
        break
for i in range(len(ch)):
    if moves[-1] - moves[-2] == i-moves[-1]:
        word += ch[i]
        moves.append(i)
if word[-1] == '.':
    print(word)
else:
    print('В конце дожна быть точка!!! ')