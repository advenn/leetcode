class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        left_edge = -2 ** 31
        right_edge = 2 ** 31 - 1

        def divider(dividend_, divisor_):
            quotient_ = 0
            while dividend_ >= divisor_:
                dividend_ -= divisor_
                quotient_ += 1
            return quotient_

        if abs(dividend) < abs(divisor):
            return 0
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > left_edge:
                return 0 - dividend
            else:
                return right_edge

        if dividend > 0 and divisor > 0:
            negative = False
        elif dividend < 0 and divisor < 0:
            negative = False
        else:
            negative = True
        if abs(dividend) == abs(divisor):
            if negative:
                return 0 - 1
            else:
                return 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        str_dividend = str(dividend)
        quotient = ''
        index = 0
        modulo = ''
        number = str_dividend[index]
        while True:
            number = int(modulo + number)
            if number < divisor:
                modulo = str(number)
                quotient += '0'
                index += 1
                if index == len(str_dividend):
                    break
                number = str_dividend[index]
            else:
                quotient += str(divider(number, divisor))
                modulo = str(number % divisor)
                index += 1
                if index == len(str_dividend):
                    break
                number = str_dividend[index]
        quotient = int(quotient)
        print('quotient:', quotient)
        print('modulo:', modulo)
        print('number:', number)
        print('index:', index)
        print("is_negative:", negative)
        if negative:
            quotient = 0 - quotient
        if left_edge < quotient < right_edge:
            return quotient
        else:
            return right_edge

s = Solution()
print(s.divide(10, -10))
