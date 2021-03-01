
def get_jokes(n):
    """Принимает на вход n - количество шуток, возвращает список из n шуток,
    сформированных из вшитых наборов слов"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    from random import randint
    res = []
    for i in range(n):
        res.append(nouns[randint(0,4)] + ' ' + adverbs[randint(0,4)] + ' ' + adjectives[randint(0,4)])
    return res

print(get_jokes(7))
