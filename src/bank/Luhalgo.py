def Luhn(card_number):

        sum = 0
        for i, c in enumerate(card_number):
            num = (2 - (i % 2)) * int(c)
            sum += int(num / 10) + (num % 10)
        # print sum
        return ((sum % 10) == 0)