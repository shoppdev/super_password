

def check_letter(letter):
    ascii_num = int(ord(letter))

    if ascii_num >=65 and ascii_num <=95:
        print('big letter')
    elif ascii_num >= 97 and ascii_num <=122:
        print('little letter')
    elif ascii_num >=48 and ascii_num <=57 :
        print('number')
    else:
        print('symbol')


    # get letter
    # get ascii code
    #print(ord(letter))
    # modify letter based on ascii


def leet_it(word):
    for letter in word:
        check_letter(letter)


if __name__ == '__main__':
    leet_it('p2Kh57$Ujk')