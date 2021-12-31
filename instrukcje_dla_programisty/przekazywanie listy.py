def greet_ussers(names):
    """Wyświetla powitanie każdemu uzytkownikowi"""
    for name in names:
        msg = f"Witaj {name.title()}"
        print(msg)


username = ['halina', 'tomek', 'marzena']
greet_ussers(username)
