#!/usr/bin/python3
import string
text = """ The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! """
text = text.lower()
for char in string.punctuation:
    text = text.replace('.' , ' ')
    text = text.replace(',' , ' ')
words = text.split() 
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print("10 самых частых слов:")
for _ in range(10):
    if not word_counts:
        break

    max_key = None
    max_value = -1
    for key in word_counts:
        if word_counts[key] > max_value:
            max_value = word_counts[key]
            max_key = key
        print(f"{max_key}: {max_value}")
        del word_counts[max_key]
