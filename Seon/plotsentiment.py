import csv
import matplotlib.pyplot as plt

final_dictionary = {}

final_dictionary['positive'] = 0
final_dictionary['neutral'] = 0
final_dictionary['negative'] = 0

with open('nltk_output.txt', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter='\t')
   
    for row in csv_reader:
        txt = row[0]
        sentiment = float(row[1])

        if sentiment == 0:
            final_dictionary['neutral'] = final_dictionary['neutral'] + 1
        elif sentiment > 0:
            final_dictionary['positive'] = final_dictionary['positive'] + 1
        else:
            final_dictionary['negative'] = final_dictionary['negative'] + 1


print("# of tweets labeled as positive: ", final_dictionary['positive'])
print("# of tweets labeled as neutral: ", final_dictionary['neutral'])
print("# of tweets labeled as negative: ", final_dictionary['negative'])

plt.figure(figsize=(5, 5))

plt.title('Sentiment Distribution of Tweets -- NLTK')
plt.xlabel('sentiment')
plt.ylabel('# of tweets per sentiment')

plt.bar(final_dictionary.keys(), final_dictionary.values(), width=0.3, color='r')

plt.show()