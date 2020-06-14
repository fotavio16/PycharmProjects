from nltk.book import *
'''
text7.concordance("dollars")
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
print(saying)
tokens = set(saying)
print(tokens)
tokens = sorted(tokens)
print(tokens)
print(tokens[-2:])

fdist1 = FreqDist(text1)
vocabulary1 = fdist1.keys()
#vocabulary1[:50]
fdist1.plot(50, cumulative=True)
#print(sorted([w for w in set(text1) if len(w) > 7 and fdist1[w] > 20]))
text1.collocations()
'''