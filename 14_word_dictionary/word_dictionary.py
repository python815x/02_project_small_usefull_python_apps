from PyDictionary import PyDictionary as pdict

dictionary = pdict('Eyes', 'Independent', 'Head', 'Yes')
print(dictionary.printSynonyms())


# while True:
#     word = input('Enter your word : ')
#     if word == '':
#         break
#
#     print(dictionary.meaning(word))