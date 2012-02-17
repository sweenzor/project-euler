#!/usr/bin/env python


# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 
# 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in
# compliance with British usage.


engl = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 
        6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
        16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
        70:'seventy', 80:'eighty', 90:'ninety', 1000:'one thousand'}

for n in range(1,10):
    engl[n*100] = engl[n]+' hundred'


def count_total(num):
    count = 0
    for n in range(1,num+1):
        print builder(n)
        count += count_letters(builder(n))
    return count


def count_letters(phrase):
    count = 0
    for word in phrase:
        count += len(word.replace(' ', ''))
    return count


def builder(num):
    # check for a match against the roots
    if num in engl:
        return engl[num]

    working = num
    phrase = []
    for place in range(1,len(str(num))+1):
        sub = str(working)[-place:]
        try:
            phrase.append(engl[int(sub)])
            working = working - int(sub)
        except:
            pass

    # hack for 'and'
    if len(phrase) > 1:
        if num > 100:
            phrase.append('and')

    phrase.reverse()
    return phrase


print count_total(5)
print count_letters(builder(115))
print count_letters(builder(342))
print count_total(1000)