import operator

infile = open('words.txt', 'r')
content = infile.read()

wordlist = content.split()
infile.close()

unsolved = True
counter = 1
used_letters = []

while(unsolved):
    print()
    print('==============================================================')
    print('Starting turn ' + str(counter) + ': ')
    greenbool = input('Any Greens? (y/n) ')
    while(greenbool == 'y'):
        loc = int(input('Location of green? (1, 2, 3, 4, 5) ')) - 1
        letter = input('What letter is the green? ').lower()
        used_letters.append(letter)

        filtered = []

        for word in wordlist:
            if (word[loc] == letter):
                filtered.append(word)
        wordlist = filtered

        print()
        greenbool = input('Any other greens? (y/n) ')
    print()

    yellowbool = input('Any yellows? (y/n) ')
    while(yellowbool == 'y'):
        loc = int(input('Location of yellow? (1, 2, 3, 4, 5) ')) - 1
        letter  = input('What letter is the yellow? ').lower()
        used_letters.append(letter)

        filtered = []

        for word in wordlist:
            if letter in word:
                if (word[loc] != letter):
                    filtered.append(word)
        wordlist = filtered

        print()
        yellowbool = input('Any other yellows? (y/n) ')
    print()

    rem_let = input('Enter ruled out letters delimitted by a space: ("a b c") ')
    rem_list = rem_let.split(' ')
    for letter in rem_list:
        used_letters.append(letter)
    
    filtered = []

    for word in wordlist:
        word_valid = True
        for letter in rem_list:
            if letter in word:
                word_valid = False
        if(word_valid):
            filtered.append(word)
    wordlist = filtered
    print()

    letter_dict = {}
    for word in wordlist:
        for letter in word:
            if(letter not in used_letters):
                if letter in letter_dict:
                    letter_dict[letter] = letter_dict[letter] + 1
                else:
                    letter_dict[letter] = 1
    
    sorted_letter_dict = sorted(letter_dict.items(), key=operator.itemgetter(1), reverse=True)
    print('Most common letters in remaining words: ')
    print(sorted_letter_dict)


    print(sorted(wordlist))
    counter += 1

    print()
    status = input('Solved? (y/n) ')
    if(status == 'y'):
        unsolved = False