# Time: O(1)
# Space: O(1)


class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman = ""

        for int_val in int_to_roman_map.keys():
            while num >= int_val:
                num -= int_val
                roman += int_to_roman_map[int_val]

        return roman
