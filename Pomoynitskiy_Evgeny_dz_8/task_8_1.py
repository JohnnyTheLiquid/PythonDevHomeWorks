valid_email = 'someone@geekbrains.ru'
non_valid_email = 'someone@geekbrainsru'

def email_parse(email_address):
    """Простой вариант проверки email, полная версия рег выражения для всех допустимых
    вариантов слишком тяжеловесна. Задача показать работоспособный код для примеров в задании"""
    import re
    RE_EMAIL = r'\w+@\w+\.\w{2,}'
    match = re.fullmatch(RE_EMAIL, email_address)
    if match:
        return {'username': email_address.split('@')[0], 'domain': email_address.split('@')[1]}
    else:
        raise ValueError(f'wrong email: {email_address}')

print(email_parse(valid_email))
print(email_parse(non_valid_email))