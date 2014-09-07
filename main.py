__author__ = 'onotole'


def lookingForSubString(number):
    if number[0] == '0':
        rangeMax = '1' + number
    else: rangeMax = number
    currentNumber = '1'
    position = 1
    for i in range(2,int(rangeMax)+1):
        for digit in str(i):
            currentNumber += digit
            if len(str(currentNumber)) > len(number):
                currentNumber = currentNumber[1:]
                position += 1
            if currentNumber == number:
                return position

if __name__ == "__main__":
    number="6789"
    number=input()
    print(lookingForSubString(number))