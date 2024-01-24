import random 
import os
import string
import sys

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "&"]

delimiters = "\t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret


def process(userID):
    indexes = getIndexes(userID)
    titles = sys.stdin.readlines()

    def split_on_multiple_chars(string_to_split, set_of_chars_as_string):
        s = string_to_split
        chars = set_of_chars_as_string

        if len(chars) == 0:
            return [s]

        ss = s.split(chars[0])
        bb = []
        for e in ss:
            aa = split_on_multiple_chars(e, chars[1:])
            bb.extend(aa)
        return bb

    def cleanup_and_count(title, delimiters, stopWordsList):
        words = split_on_multiple_chars(title, delimiters + '\n')

        cleaned_words = [word.lower() for word in words if word.lower() not in stopWordsList and word.lower() != '']
        return cleaned_words

    titlesIndexed = []
    for idx in indexes:
        titlesIndexed += cleanup_and_count(titles[idx], delimiters, stopWordsList)

    # Calculate word count
    wordCount = {}
    for word in titlesIndexed:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    # Sort by descending count and ascending word lexicography
    sorted_wordCount = sorted(wordCount.items(), key=lambda x: (-x[1], x[0].lower()))

    for i, (word, count) in enumerate(sorted_wordCount[:20]):
        print(f"{word}")

process(sys.argv[1])