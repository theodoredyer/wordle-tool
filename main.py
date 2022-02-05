infile = open('words.txt', 'r')
content = infile.read()

wordlist = content.split()
infile.close()

unsolved = True
counter = 1

while(unsolved):
    print()
    print('Starting turn ' + str(counter) + ': ')
    greenbool = input('Any Greens? (y/n) ')
    while(greenbool == 'y'):
        loc = int(input('Location of green? (1, 2, 3, 4, 5) ')) - 1
        letter = input('What letter is the green? ').lower()

        filtered = []

        for word in wordlist:
            if (word[loc] == letter):
                filtered.append(word)
        wordlist = filtered

        greenbool = input('Any other greens? (y/n) ')

    yellowbool = input('Any Yellows? (y/n) ')
    while(yellowbool == 'y'):
        loc = int(input('Location of yellow? (1, 2, 3, 4, 5) ')) - 1
        letter  = input('What letter is the yellow? ').lower()

        filtered = []

        for word in wordlist:
            if letter in word:
                if (word[loc] != letter):
                    filtered.append(word)
        wordlist = filtered

        yellowbool = input('Any other yellows? (y/n) ')

    print(sorted(wordlist))
    counter += 1

    status = input('Solved? (y/n) ')
    if(status == 'y'):
        unsolved = False