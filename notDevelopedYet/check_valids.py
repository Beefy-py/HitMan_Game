def valid_name(name):
    if ' ' in name.split():
        return 'un_valid'
    if len(name) < 3:
        return 'un_valid'
    else:
        return 'valid'


def valid_gender(gender):
    if gender != gender.capitalize():
        return 'un_valid'
    elif not gender or gender is None:
        return 'un_valid'
    else:
        return 'valid'


def valid_birth_date(birth_date):
    if len(birth_date.split()):
        return 'un_valid'















