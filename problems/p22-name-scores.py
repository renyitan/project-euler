"""
Problem 22 - Names Scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""


def run():

    with open('p022_names.txt') as f:
        for line in f:
            names = line.split(",")
            names = [name.lower().strip('"') for name in names]
            break

    names.sort()

    total = 0
    for index, name in enumerate(names):
        # txt file is 1-index, names[] is 0-indexed
        total += calculate_score(name, index+1)
    return total


def calculate_score(name, pos):
    score = 0
    for ch in name:
        score += (ord(ch)-ord('a') + 1)
    return score * pos


if __name__ == "__main__":
    print(run())
