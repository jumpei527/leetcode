class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        fraction = []
        if numerator * denominator < 0:
            fraction.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        fraction.append(str(numerator//denominator))
        remainder = numerator % denominator

        if remainder != 0:
            fraction.append(".")

        seen_remainder = {}
        while remainder != 0:
            remainder *= 10
            quotient = remainder // denominator
            remainder = remainder % denominator
            fraction.append(str(quotient))

            if remainder in seen_remainder:
                start_index = seen_remainder[remainder]
                fraction.insert(start_index, "(")
                fraction.append(")")
                break

            seen_remainder[remainder] = len(fraction)

        return "".join(fraction)
