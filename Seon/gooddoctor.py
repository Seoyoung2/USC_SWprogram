import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import OrderedDict
import operator


final_dictionary = {}

with open('GoodDoctorWeek1_clean.csv', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        if line_count == 1:
            line_count = line_count + 1
        else:
            line_count = line_count + 1
            # text는 첫번째 행이니까 row[0]
            txt = row[0]
            
            final_txt = txt.lower()
            stop_words = set(stopwords.words('english'))
            tokenizer = RegexpTokenizer('r\w+')
            word_tokens = tokenizer.tokenize(final_txt)
            filtered_sentence = [w for w in word_tokens if not w in stop_words]

            for w in filtered_sentence:
                if w not in final_dictionary:
                    final_dictionary[w] = 1
                else:
                    final_dictionary[w] = final_dictionary[w] + 1
                    
sorted_d = sorted(final_dictionary.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d)
