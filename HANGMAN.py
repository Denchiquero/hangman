import random
import os

rus_txt = open('dict.txt', 'r', encoding="utf-8")
eng_txt = open('engwords.txt', 'r', encoding="utf-8")

rus_lan = ['Русский', 'русский', 'Heccrbq', 'heccrbq']
eng_lan = ['English', 'english', 'Утпдшыр', 'утпдшыр']

wordlist_1 = []
wordlist_2 = []
wordlist_3 = []

rus_dict = {'welcome_word': """Привет! Добро пожаловать в игру Виселица!
Правила просты: я загадал слово, а ты должен его угадать.
Но учти, что за каждой ошибкой следует наказание!
У тебя будет 9 попыток. По истечении их запаса тебя повесят) 
Желаю тебе удачи!""",
            'wordlist_1': wordlist_1,
            'wordlist_2': wordlist_2,
            'wordlist_3': wordlist_3,
            'choose_lev': 'Выбери уровень игры: 1, 2, 3',
            'hello_again': ['Что ж, еще разок!', 'Заново!', 'На спавн!', 'Ах щит! Хи ви го эгейн!'],
            'not_guess': ['Неее', 'Неверно', 'А подумать?'],
            'guessed': ['Правильно!', 'Так держать!', 'Молодец!', 'Ты угадал!', 'В точку!'],
            'happy': 'О! Рад видеть тебя снова!',
            'you_won': '\nТы выиграл!',
            'call_a_letter': '\n\nНазови букву: ',
            'turns_left': 'Осталось попыток: ',
            'used': 'Использованные буквы: ',
            'game_over': '\n\nТы проиграл! Это слово: ',
            'one_more': 'Сыграем еще раз?(да/нет)',
            'again': ['да', 'Да', 'ДА', 'if', 'If', 'IF'],
            'already_used': 'Вы уже использовали эту букву. Попробуйте другую',
            'scored' : 'Вы набрали: '
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
            'guessed': ['Right!', 'Keep it up!', 'Well done!', 'You guessed!', 'Exactly!'],
            'happy': 'Wow! glad to see you again!',
            'you_won': '\n\nYou win!',
            'call_a_letter': '\n\nName a letter: ',
            'turns_left': 'Turns left: ',
            'used': 'Used letters: ',
            'game_over': '\n\nGame over! The word is: ',
            'one_more': 'Do you wanna play one more time?(yes/no)',
            'again': ['yes', 'Yes', 'YES', 'нуы', 'Нуы', 'НУЫ'],
            'already_used': 'You have already used this letter. Try another one',
            'scored' : 'You scored: '
            }


def sortirovka():
    for i in dictionary:
        match len(i):
            case 3|4|5:
                wordlist_1.append(i)
            case 6|7|8|9:
                wordlist_2.append(i)
            case 10|11|12|13|14|15|16|17|18:
                wordlist_3.append(i)


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
    global dictionary
    if lan in rus_lan:
        dictionary = rus_txt.read().split()
        return rus_dict
    elif lan in eng_lan:
        dictionary = eng_txt.read().split()
        return eng_dict


def level(lev):
    sortirovka()
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


def man():
    global word, turns
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
            print(f'{dict_lan['game_over']}', word)
            print(f'{dict_lan['scored']}', score)


def hangman():
    global games, answer, turns, word, score
    games += 1
    if games == 2:
        print(f'{dict_lan['happy']}')
    elif games >= 3:
        print(f'{random.choice(dict_lan['hello_again'])}')
    lev = input(f'{dict_lan['choose_lev']}\n')
    wordlist = level(lev)
    word = random.choice(wordlist)
    alphabet = []
    guesses = ''
    os.system('cls||clear')
    turns = 9
    while turns > 0:
        missed = 0
        for letter in word:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                missed += 1
        if missed == 0:
            print(f'{dict_lan['you_won']}')
            score += 1
            break
        guess = input(f'{dict_lan['call_a_letter']}')
        os.system('cls||clear')
        if guess not in guesses:
            guesses += guess
            alphabet.append(guess)
            if guess not in word:
                turns -= 1
                print(f'{random.choice(dict_lan['not_guess'])}')
                print(f'{dict_lan['turns_left']}', turns)
                print(f'{dict_lan['used']}', ' '.join(alphabet))
                man()
            else:
                print(f'{random.choice(dict_lan['guessed'])}')
                print(f'{dict_lan['turns_left']}', turns)
                print(f'{dict_lan['used']}', ' '.join(alphabet))
                man()
        else:
            print(f'{dict_lan['already_used']}')
            print(f'{dict_lan['turns_left']}', turns)
            print(f'{dict_lan['used']}', ' '.join(alphabet))
            man()

    answer = input(f'{dict_lan['one_more']}')


answer = ''
games = 0
dict_lan = {}
word = ''
turns = 0
score = 0


def main():
    print('HANGMAN.PY ver. 1.7 \n\U000000A9 Denis Krutov. All rights reversed')

    language()


if __name__ == "__main__":
    main()
