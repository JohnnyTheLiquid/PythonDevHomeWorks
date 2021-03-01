names_1 = ["Иван", "Мария", "Петр", "Илья", "Павел", "Михаил"]
names_2 = ["Иван", "Мария", "Петр", "Илья"]

def thesaurus(names):
    """Принимает на вход список имен, возвращает словарь, где ключ - первая буква
    значение - список имен, начинающихся на эту букву"""
    for idx, name in enumerate(names):
        names[idx] = [name]

    thes = {}
    for name in names:
        if name[0][0] in thes.keys():
            thes[name[0][0]].append(name[0])
        else:
            thes[name[0][0]] = (name)
    return thes

print (thesaurus(names_1))
print(thesaurus(names_2))
