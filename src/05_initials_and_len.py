name = input('ФИО: ').strip().title()
initials = name.split()
initials = ''.join(initials[0] for initials in initials)



print(len(f'{name}'), initials)