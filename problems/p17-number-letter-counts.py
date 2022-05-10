"""
Problem 17 - Number Letter Count

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}


def run():
    start, end = 1, 1000
    count = 0
    for n in range(start, end+1):
        s = get_number_letter(n)
        s = "".join([ch for ch in s.strip() if ch.isalpha()])
        count += len(s)
    return count


def get_number_letter(n):
    """
    Returns the english words for number, n
    Example: 120 => "one hundred and twenty"
    """
    digits = [int(ch) for ch in str(n)]
    tenths = 1
    res = []

    while digits:
        digit = digits.pop()
        # check for special case where it's [10 - 19]
        if tenths == 1 and digits and digits[-1] == 1:
            next = digits.pop()
            digit += next*10
            res.append(dict[digit])
            tenths *= 100
            continue
        elif tenths == 1 and digit != 0:
            res.append(dict[digit])
        elif tenths == 10 and digit != 0:
            res.append(dict[digit*10])
        elif tenths == 100 and digit != 0:
            if res:
                res.append('and')
            res.append('hundred')
            res.append(dict[digit])
        elif tenths == 1000 and digit != 0:
            if res:
                res.append('and')
            res.append('thousand')
            res.append(dict[digit])
        tenths *= 10
    return " ".join(res[::-1])


if __name__ == "__main__":
    print(run())
