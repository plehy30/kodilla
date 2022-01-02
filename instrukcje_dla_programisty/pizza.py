# def make_pizza(size, *dodatki):
#     """Wyświetlanie dodatków"""
#     print(f"Zamawiam pizzę o wielkości {size} z dodatkami:")
#     for dodatek in dodatki:
#         print(f"- {dodatek}")
#
#
# make_pizza(40, 'szynka', 'ser', 'mozzarella')
#

# def buil_profile(first, last, **user_info):
#     """Budowa słownika zawierajacego wszelkie informację o użytkowniku"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_profile = buil_profile('Albert', 'Einstein', location='Pricenton', field='fizyka')
# print(user_profile)
def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszelkie informacje o użytkowniku."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='fizyka')
print(user_profile)


def sandwich(*items):
    for item in items:
        print(f"Dodałem do twojej kanapki {item}")
    print(f"Twoja kanapka jest gotowa")


sandwich("chleb", 'masło', 'szynka')


def make_car(marka, model, **options):
    wybor_car = {'marka': marka.title(), 'model': model.title()}
    for option, value in options.items():
        wybor_car[option] = value
    return wybor_car


my_car = make_car('volvo', 's60', color='blue', year='new')
print(my_car)
