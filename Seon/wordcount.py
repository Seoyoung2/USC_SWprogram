import csv
import nltk
from nltk.tokenize import word_tokenize
#ltk.download()
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import OrderedDict
import operator

example_sentence = "This is a simple sentence."

word_tokens = word_tokenize(example_sentence)

for w in word_tokens:
    print(w)
print("==========================")

example_sentence1 = "It's a simple sentence."

tokenizer = RegexpTokenizer(r'\w+')
word_tokens = tokenizer.tokenize(example_sentence1)

for w in word_tokens:
    print(w)
print("==========================")


final_dictionary = {}

with open('Data.csv', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        
        if line_count == 1:
            line_count = line_count + 1
        else:
            line_count = line_count + 1
            txt = row[1]
            
            final_txt = txt.lower()
            stop_words = set(stopwords.words('English'))
            tokenizer = RegexpTokenizer(r'\w+')
            word_tokens = tokenizer.tokenize(final_txt)
            filtered_sentence = [w for w in word_tokens if not w in stop_words]


            for w in filtered_sentence:
                if w not in final_dictionary:
                    final_dictionary[w] = 1
                else:
                    final_dictionary[w] = final_dictionary[w] + 1
                    
sorted_d = sorted(final_dictionary.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d)


with open('wordCount.csv', mode='w', newline = '', encoding='UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter=',')
    
    my_writer.writerow(['Word', 'Count'])
    
    for key in sorted_d:
        current_Word = str(key[0])
        current_Count = int(key[1])
        
        my_writer.writerow([current_Word, current_Count])