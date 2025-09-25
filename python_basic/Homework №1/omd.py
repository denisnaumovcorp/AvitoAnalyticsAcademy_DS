# Guido van Rossum <guido@python.org>
import random

def step2_umbrella():
    print('Утка-маляр 🦆 взяла зонтик и пошла в бар. ☂️')
    if random.random() < 0.3:
        print('После бара пошёл дождь! 🌧️')
        print('Утка осталась сухой благодаря зонтику и не заболела! 🦆✅')
    else:
        print('Погода была хорошая, зонтик не пригодился. ☀️')
    if random.random() < 0.05:
        print('Внезапно началась драка! ⚔️')
        print('Что делать? 1 - Защищаться зонтиком, 2 - Убежать')
        choice = input('Выберите: 1/2: ')
        if choice == '1':
            print('Утка смогла защититься зонтиком! 🦆🛡️')
        else:
            print('Утка убежала, но потеряла зонтик! 🏃‍♀️')
    else:
        print('Вечер прошёл спокойно. 😌')
    print('Утка хорошо отдохнула и вернулась домой, всё прошло без проишествий. 🏠')

def step2_no_umbrella():
    print('Утка-маляр 🦆 не взяла зонтик и пошла в бар.')
    if random.random() < 0.4:
        print('После бара пошёл дождь! 🌧️')
        print('Утка промокла и простудилась! 🤧🦆')
    else:
        print('Погода была хорошая, зонтик не понадобился. ☀️')
    if random.random() < 0.15:
        print('Утка случайно забрала чей-то зонтик! 😅☂️')
        print('Что делать? 1 - Вернуть зонтик, 2 - Оставить себе')
        choice = input('Выберите: 1/2: ')
        if choice == '1':
            print('Утка вернула зонтик владельцу! 👏')
        else:
            print('Утка оставила зонтик себе! 😈')
    else:
        print('Утка вернулась домой без зонтика. 🏠')
    print('Утка хорошо отдохнула и вернулась домой, всё прошло без проишествий. 🏠')

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

if __name__ == '__main__':
    step1()