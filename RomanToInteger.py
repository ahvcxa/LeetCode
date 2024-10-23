class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        start = 0
        length = len(s)

        while start < length:
            if start + 1 < length and roman_numerals[s[start]] < roman_numerals[s[start + 1]]:
                result -= roman_numerals[s[start]]
            else:
                result += roman_numerals[s[start]]
            start += 1
        return result
        
