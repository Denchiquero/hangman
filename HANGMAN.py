import random

rus_dict = {}

def language():
    lan = input("""\nPlease select game language
Пожалуйста, выберите язык игры
(English/Русский)\n""")

    if lan == 'English':
        print("""Hello! Welcome to Hangman game!
The rules are simple: I have thought of a word and you have to guess it.
But remember that for every mistake you get a punishment!
You have 5 attempts. When they are over, you will be hanged) 
Good luck!""")
        hangmaneng()
        while answer == 'yes':
            changelan = input('Do you want to change language?(yes/no)')
            if changelan == 'yes':
                hangmanrus()
            else:
                hangmaneng()
        else:
            print('Bye!')

    elif lan == 'Русский':
        print("""Привет! Добро пожаловать в игру Виселица!
Правила просты: я загадал слово, а ты должен его угадать.
Но учти, что за каждой ошибкой следует наказание!
У тебя будет 9 попыток. По истечении их запаса тебя повесят) 
Желаю тебе удачи!""")
        hangmanrus()
        while answer == 'да':
            changelan = input('Хочешь поменять язык?(да/нет)')
            if changelan == 'да':
                hangmaneng()
            else:
                hangmanrus()
        else:
            print('Пока!')
    else:
        print("""Sorry, this game doesn't support this language
Простите, эта игра не поддерживает этот язык""")


def level(lev):
    if lev == '1':
        return wordlist1
    if lev == '2':
        return wordlist2
    if lev == '3':
        return wordlist3


def leveleng(lev):
    if lev == '1':
        return wordlist4
    if lev == '2':
        return wordlist5
    if lev == '3':
        return wordlist6


def hang():
    print(""" |
\U0001F635
/|\\
 |
/ \\""")


wordlist1 = [
wordlist2 = 
wordlist3 = 
wordlist4 = ['bed', 'cat', 'egg', 'room', 'son', 'han', 'wine', 'song', 'pen', 'cup']
wordlist5 = ['carpet', 'amigo', 'mother', 'apple', 'window', 'clock', 'potato', 'school', 'rubber', 'tender']
wordlist6 = ['wardrobe', 'percent', 'snowfall', 'chemistry', 'happiness', 'pudding', 'bathroom', 'doorbell',
             'grandfather', 'relaxation']


def hangmanrus():
    global games
    global answer
    global changelan
    games += 1
    if games == 2:
        print('О! Рад видеть тебя снова!')
    elif games == 3:
        print('Что ж, еще разок!')
    elif games > 3:
        print('Заново!')
    lev = input('Выбери уровень игры: 1, 2, 3\n')
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
            print('\nТы выиграл!')
            break
        guess = input('\n\nНазови букву: ')
        alphabet.append(guess)
        guesses += guess
        if guess not in secret:
            turns -= 1
            print('\nНе угадал.')
            print('Осталось попыток: ', turns)
            print('Использованные буквы:', ' '.join(alphabet))
            if turns == 8: print('\n | ')
            if turns == 7: print(' |\n\U0001F642 ')
            if turns == 6: print(' |\n\U0001F610 \n |')
            if turns == 5: print(' |\n\U0001F62C \n | \n |')
            if turns == 4: print(' |\n\U0001F61E \n | \n | \n/')
            if turns == 3: print(' |\n\U0001F974 \n | \n | \n/ \\')
            if turns == 2: print(' |\n\U0001F628 \n/| \n | \n/ \\')
            if turns == 1: print(' |\n\U0001F628 \n/|\\ \n | \n/ \\')
            if turns == 0: hang()
            if turns == 0: print('\n\nТы проиграл! Это слово: ', secret)
        else:
            print('Использованные буквы:', ' '.join(alphabet))

    answer = input('Сыграем еще раз?(да/нет)')


def hangmaneng():
    global games
    global answer
    global changelan
    games += 1
    if games == 2:
        print('Wow! Glad to see you again!')
    elif games == 3:
        print('Well, one more time!')
    elif games > 3:
        print('Again!')
    lev = input('Choose your level: 1, 2, 3\n')
    wordlist = leveleng(lev)
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
            print('\nYou win!')
            break
        guess = input('\n\nGuess a letter: ')

        alphabet.append(guess)

        guesses += guess

        if guess not in secret:
            turns -= 1
            print('\nNope.')
            print('Attempts left: ', turns)
            print('Used letters:', ' '.join(alphabet))
            if turns == 8: print('\n | ')
            if turns == 7: print(' |\n\U0001F642 ')
            if turns == 6: print(' |\n\U0001F610 \n |')
            if turns == 5: print(' |\n\U0001F62C \n | \n |')
            if turns == 4: print(' |\n\U0001F61E \n | \n | \n/')
            if turns == 3: print(' |\n\U0001F974 \n | \n | \n/ \\')
            if turns == 2: print(' |\n\U0001F628 \n/| \n | \n/ \\')
            if turns == 1: print(' |\n\U0001F628 \n/|\\ \n | \n/ \\')
            if turns == 0: hang()
            if turns == 0: print('\n\nGame over! The word is: ', secret)
        else:
            print('Here is your alphabet:', ' '.join(alphabet))
    answer = input('Do you want to play one more time?(yes/no)')

def main():
    print("""HANGMAN.PY ver. 1.3
    \U000000A9 Denis Krutov. All rights reversed""")

    answer = ''
    games = 0

    language()
    
if __name__ == "__main__":
	main()
