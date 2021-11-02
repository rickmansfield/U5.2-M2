# see assets for enumerate
alpha = "qwertyuiopasdfghjklzxcvbnm"
# order = {}
# for i, char in enumerate(alpha):
#     order[char] = i

# print(order)

"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).
You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.
The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".
Example 1:
```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```
Example 2:
```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```
Example 3:
```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```
Notes:
- order.length == 26
- All characters in words[i] and order are English lowercase letters.


make a dictionary the map between the letters and thier order

iterate over the words extracting the index ending the iterations at len - 2
  extract word1 and word2 from the list of words using i and i+1 respectively

  iterate over a range of the length of the shorted of word1 and word2 
  extracting an indwex of j
    check if the word1[j] is not equal to the word2[j]
      if the order_dict[word1[j]] is greater than the order_dic[word2[j]]...
        return false to the caller
      break
  otherwise...
    check if the lenght of word1 is greater than the length of word2 
      return false to the caller

if we get here return true to the caller
"""


def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str
    Output:
    bool
    """

    order_dict = {}
    for i, char in enumerate(alpha_order):
        order_dict[char] = i

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if order_dict[word1[j]] > order_dict[word2[j]]:
                    return False
                break

            else:
                if len(word1) > len(word2):
                    return False

    return True

# alternative solution


# def are_words_sorted(words, alpha_order):
#     dictionary = {}
#     alphabetical = True
#     for word in words:
#         for letter in range(len(word)):
#             if letter == 0:
#                 dictionary[word] = str(alpha_order.index(word[letter]))
#             else:
#                 dictionary[word] += str(alpha_order.index(word[letter]))
#     listed = list(dictionary.values())
#     for i in range(len(listed)-1):
#         if listed[i] > listed[i+1]:
#             alphabetical = False
#     return alphabetical


words = ["lambda", "school"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(are_words_sorted(words, order))  # > True

words = ["were", "where", "yellow"]
order = "habcdefgijklmnopqrstuvwxyz"
print(are_words_sorted(words, order))  # > False

words = ["lambda", "lamb"]
order = "abcdefghijklmnopqrstuvwxyz"
print(are_words_sorted(words, order))
