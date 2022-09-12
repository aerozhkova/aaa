# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка не промокла, потому что взяла зонт.'
    )


def step2_no_umbrella():
    print(
        'Утка все равно не промокла, потому что ее крылья смазаны жиром. ' 
        'Не переживай.'
    )


if __name__ == '__main__':
    step1()
