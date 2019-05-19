def convert_to_words(input_message):
    # Vocabulary
    words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',  # issue spotted
        '6': 'six',
        '7': 'seven',  # issue spotted
        '8': 'eight',
        '9': 'nine',
        '=': 'equals',
        '-': 'minus',
        '+': 'plus',
        '*': 'times',
        '/': 'divided by',
        '.': 'point',  # added this value for future improvement
        ',': 'comma',
        ' ': ' '  # to be able to iterate through the input string with " "
    }

    decimals = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
    }

    billions = {
        1: 'hundred',
        2: 'thousand',
        3: 'million',
        4: 'billion ',
        5: 'trillion'
    }

    # Check if the input message is valid
    if type(input_message) == str:

        # Now lets split the input string and iterate over the separate digits:
        digits = input_message.split()

        # Checking if only there are no alphabetic symbols in our input message
        # Probably we can import the alphabet from string.py - we will see later
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%&'
        for item in digits:
            for symbol in item:
                if symbol in alphabet:
                    return 'Letter spotted. Invalid input - Only digits and math signs accepted'

        # Define an inner function to humanize numbers like 23, 67 and etc
        def two_digits(two_number):
            # for digits like 40 & 50
            if two_number[1] == '0':
                return decimals[two_number[0]]

            # for digits like 11 & 15
            elif (two_number[0] == '1') and (two_number in decimals):
                return decimals[two_number]

            # for 3 digit case like 209 & 502
            elif two_number[0] == '0':
                return words[two_number[1]]
            else:
                return decimals[two_number[0]] + ' ' + words[two_number[1]]

        # Define an inner function to humanize numbers like 253, 967 and etc
        def three_digits(three_number):
            if three_number[0] != '0' and three_number[1] == three_number[2] == '0':
                outcome_three = words[three_number[0]] + ' ' + billions[1]
            elif three_number[0] == '0':
                outcome_three = ''
            else:
                outcome_three = words[three_number[0]] + ' ' + billions[1] + ' ' + two_digits(three_number[1:3])
            return outcome_three

        for element in digits:

            length_of_the_element = len(element)
            # I have established the limitation up to 12 symbols per digit,
            # same as ordinary calculators - to avoid use of sextillions and etc
            if length_of_the_element > 12:
                return 'Digits to long; Try shorter one, m8'

            # Work with long figures
            elif length_of_the_element > 3:
                aggregate = ''
                amount_of_groups = length_of_the_element // 3

                # Case when we have no remainder after grouping by 3 symbols
                if (length_of_the_element % 3) == 0:
                    for group in range(amount_of_groups):
                        aggregate += three_digits(element[3*group: 3 + 3 * group]) + ' ' + billions[amount_of_groups - group] + ' '
                    # Stupid fix, need future improvement
                    aggregate = aggregate[:len(aggregate)-8]

                # Case when we have a remainder after grouping by 3 symbols (1 or 2 digits)
                elif (length_of_the_element % 3) > 0:
                    flag = length_of_the_element % 3

                    if flag == 1:
                        aggregate += words[element[0]] + ' ' + billions[amount_of_groups+1] + ' '
                        fix = element[0]
                        element = element[1:]


                    elif flag == 2:
                        aggregate += two_digits(element[:2]) + ' ' + billions[amount_of_groups+1] + ' '
                        fix = element[:2]
                        element = element[2:]


                    for group in range(amount_of_groups):
                        aggregate += three_digits(element[3*group: 3 + 3 * group]) + ' ' + billions[amount_of_groups - group] + ' '
                    # Stupid fix, need future improvement
                    aggregate = aggregate[:len(aggregate)-8]
                    element = fix + element
                input_message = input_message.replace(element, aggregate, 1)
            elif length_of_the_element == 3:
                input_message = input_message.replace(element, three_digits(element), 1)
            elif length_of_the_element == 2:
                input_message = input_message.replace(element, two_digits(element), 1)
            elif length_of_the_element <= 1:
                if element in words:
                    input_message = input_message.replace(element, words[element], 1)
        return input_message
    else:
        return 'invalid input'


print(convert_to_words(1))
print(convert_to_words('1y'))
print ('_________________________')
print ('35 + 9 = - 559')
print(convert_to_words('35 + 9 = - 559'))
print ('_________________________')
print ('5 * 7 = 547321')
print(convert_to_words('5 * 7 = 547321'))
print ('_________________________')
print ('89 * 7 = 2987547321')
print(convert_to_words('89 * 7 = 2987547321'))
print ('_________________________')
print ('1 * 45 = 31987547321')
print(convert_to_words('1 * 45 = 31987547321'))
print ('_________________________')
print(convert_to_words('30 + 7744 = 1074343777437'))
