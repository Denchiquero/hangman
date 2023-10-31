import random

rus_lan = ['Русский', 'русский', 'Heccrbq', 'heccrbq']
eng_lan = ['English', 'english', 'Утпдшыр', 'утпдшыр']

rus_dict = {'welcome_word': """Привет! Добро пожаловать в игру Виселица!
Правила просты: я загадал слово, а ты должен его угадать.
Но учти, что за каждой ошибкой следует наказание!
У тебя будет 9 попыток. По истечении их запаса тебя повесят) 
Желаю тебе удачи!""",
            'wordlist_1': ['кот', 'чип', 'чай', 'руль', 'окно', 'небо', 'ухо'],
            'wordlist_2': ['чашка', 'лодка', 'мышка', 'класс', 'ручка', 'доска', 'кактус'],
            'wordlist_3': ['компьютер', 'итератор', 'калькулятор', 'видеокарта', 'процессор', 'программа', 'монитор'],
            'choose_lev': 'Выбери уровень игры: 1, 2, 3',
            'hello_again': ['Что ж, еще разок!', 'Заново!', 'На спавн!', 'Ах щит! Хи ви го эгейн!'],
            'not_guess': ['Неее', 'Неверно', 'А подумать?'],
            'happy': 'О! Рад видеть тебя снова!',
            'you_won': '\nТы выиграл!',
            'call_a_letter': '\n\nНазови букву: ',
            'turns_left': 'Осталось попыток: ',
            'used': 'Использованные буквы: ',
            'game_over': '\n\nТы проиграл! Это слово: ',
            'one_more': 'Сыграем еще раз?(да/нет)',
            'again': ['да', 'Да', 'ДА', 'if', 'If', 'IF']
            }

eng_dict = {'welcome_word': """Hello! Welcome to Hangman game!
The rules are simple: I have thought of a word and you have to guess it.
But remember that for every mistake you get a punishment!
You have 5 attempts. When they are over, you will be hanged) 
Good luck!""",
            'wordlist_1': ['bed', 'cat', 'egg', 'room', 'son', 'han', 'wine', 'song', 'pen', 'cup'],
            'wordlist_2': ['carpet', 'amigo', 'mother', 'apple', 'window', 'clock', 'potato', 'school', 'rubber',
                           'tender'],
            'wordlist_3': ['wardrobe', 'percent', 'snowfall', 'chemistry', 'happiness', 'pudding', 'bathroom',
                           'doorbell', 'grandfather', 'relaxation'],
            'choose_lev': 'Choose game level: 1, 2, 3',
            'hello_again': ['Well, one more time!', 'Again!', 'To the spawn!', 'Oh shit! Here we go again!'],
            'not_guess': ['Nooo', 'Wrong', 'How about thinking?'],
            'happy': 'Wow! glad to see you again!',
            'you_won': '\nYou win!',
            'call_a_letter': '\n\nName a letter: ',
            'turns_left': 'Turns left: ',
            'used': 'Used letters: ',
            'game_over': '\n\nGame over! The word is: ',
            'one_more': 'Do you wanna play one more time?(yes/no)',
            'again': ['yes', 'Yes', 'YES', 'нуы', 'Нуы', 'НУЫ']
            }


def language():
    global dict_lan
    lan = input("""\nPlease select game language
Пожалуйста, выберите язык игры
(English/Русский)\n""")

    dict_lan = selected_language(lan)

    hangman()

    while answer in dict_lan['again']:
        hangman()


def selected_language(lan):
    if lan in rus_lan:
        return rus_dict
    elif lan in eng_lan:
        return eng_dict


def level(lev):
    if lev == '1':
        return dict_lan['wordlist_1']
    if lev == '2':
        return dict_lan['wordlist_2']
    if lev == '3':
        return dict_lan['wordlist_3']


def hang():
    print(""" |
\U0001F635
/|\\
 |
/ \\""")


def hangman():
    global games
    global answer
    games += 1
    if games == 2:
        print(f'{dict_lan['happy']}')
    elif games >= 3:
        print(f'{random.choice(dict_lan['hello_again'])}')
    lev = input(f'{dict_lan['choose_lev']}\n')
    wordlist = level(lev)
    alphabet = []
    secret = random.choice(wordlist)
    guesses = ''

    turns = 9
    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                missed += 1
        if missed == 0:
            print(f'{dict_lan['you_won']}')
            break
        guess = input(f'{dict_lan['call_a_letter']}')
        alphabet.append(guess)
        guesses += guess
        if guess not in secret:
            turns -= 1
            print(f'\n{random.choice(dict_lan['not_guess'])}')
            print(f'{dict_lan['turns_left']}', turns)
            print(f'{dict_lan['used']}', ' '.join(alphabet))
            match turns:
                case 8:
                    print('\n | ')
                case 7:
                    print(' |\n\U0001F642 ')
                case 6:
                    print(' |\n\U0001F610 \n |')
                case 5:
                    print(' |\n\U0001F62C \n | \n |')
                case 4:
                    print(' |\n\U0001F61E \n | \n | \n/')
                case 3:
                    print(' |\n\U0001F974 \n | \n | \n/ \\')
                case 2:
                    print(' |\n\U0001F628 \n/| \n | \n/ \\')
                case 1:
                    print(' |\n\U0001F628 \n/|\\ \n | \n/ \\')
                case 0:
                    hang()
                    print(f'{dict_lan['game_over']}', secret)
                case _:
                    print(f'{dict_lan['used']}', ' '.join(alphabet))

    answer = input(f'{dict_lan['one_more']}')


answer = ''
games = 0
dict_lan = {}


def main():
    print("""HANGMAN.PY ver. 1.4
    \U000000A9 Denis Krutov. All rights reversed""")

    language()


if __name__ == "__main__":
    main()
if __name__ == "__main__":
	main()
