from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """ Create attack for hero and generate number. """
    if char_class == 'warrior':
        return f'{char_name} нанёс урон противнику равный {5 + randint(3, 5)}'
    if char_class == 'mage':
        return f'{char_name} нанёс дмг противнику равный {5 + randint(5, 10)}'
    if char_class == 'healer':
        return f'{char_name} дал дмг противнику равный {5 + randint(-3, -1)}'
    return None


def defence(char_name: str, char_class: str) -> str:
    """ Create defence and number. """
    if char_class == 'warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} урона'
    if char_class == 'mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
    if char_class == 'healer':
        return f'{char_name} блокировал {10 + randint(2, 5)} урона'
    return None


def special(char_name: str, char_class: str) -> str:
    """ Create special skill. """
    if char_class == 'warrior':
        return f'{char_name} применил специальное умение'
    if char_class == 'mage':
        return f'{char_name} применил специальное умение {5 + 40}»'
    if char_class == 'healer':
        return f'{char_name} применил специальное умение {10 + 30}»'
    return None


def start_training(char_name: str, char_class: str) -> str:
    """ Start training and choose hero. """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack')
    print('— чтобы атаковать противника,')
    print('defence — чтобы блокировать атаку противника')
    print('или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """ Choose type. """
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        print('Введи за кого хочешь играть: ')
        char_class = input('Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель эт воин ближнего боя. Сильный, выносливый.')
        if char_class == 'mage':
            print('Маг: воин дальнего боя. Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — Черпает силы из природы, веры и духов.')
        approve_choice = input('Впиши Y и продолжишь.').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))