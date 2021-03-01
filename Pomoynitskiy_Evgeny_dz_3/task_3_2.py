# инициализируем словарь, где ключи - англ. числительные, значения - русские
words = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
         "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

def num_translate_adv(eng):
    """Принимает на вход английское числительное, возвращает русское. Словарь предопределен"""
    if eng.lower() in words.keys():
        if eng == eng.capitalize():
            print (words[eng.lower()].capitalize())
        elif eng == eng.lower():
            print(words[eng])
    else:
        print(None)

num_translate_adv("eleven") # отсутствует в словаре
num_translate_adv("seven")
num_translate_adv('One')
