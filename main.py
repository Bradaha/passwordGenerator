import random


def passwordGen():
    lowerChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u'
                  'v', 'w', 'x', 'y', 'z']

    upperChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U',
                  'V', 'W', 'X', 'Y', 'Z']

    numChar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    specialChar = ['!', '$', '%', '&', '*']

    password = (random.choice(lowerChars) + random.choice(upperChars) + random.choice(numChar) +
                random.choice(specialChar))

    password2 = (random.choice(lowerChars) + random.choice(upperChars) + random.choice(numChar) +
                 random.choice(specialChar))

    print(password + password2)
    return password


passwordGen()
