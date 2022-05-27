from turtle import position


def find_anagram(word, anagram):

    list1 = list(word)
    list2 = list(anagram)

    list1.sort()
    list2.sort()

    position=0
    matches = True

    while position < len(word) and matches:
        if list1[position] == list2[position]:
            position = position+1
        else:
            matches = False

    return matches

word1=input("first word: ")
word2=input("second word: ")
print(find_anagram(word1, word2 ))

