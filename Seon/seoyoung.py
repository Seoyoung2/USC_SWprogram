import re
import csv
import numpy as np
from textblob import TextBlob
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import operator
import matplotlib.pyplot as plt

final_dictionary = {}
txt_list = []
daily_list = {}     #날짜별로 text 저장 (23-28)
hourly_list = {}    #시간별로 text 저장 (0-23)

for i in range(23, 29):
    daily_list[i] = []
for i in range(0, 24):
    hourly_list[i] = []

with open('GoodDoctorWeek1_clean.csv', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0

    total_sentiment = 0

    for row in csv_reader:
        if line_count == 0:
            line_count = line_count + 1
        else:
            if row[4] != '2017':
                continue

            txt = row[0]
            day = row[6]
            hour = row[7]

            txt = re.sub('@\S+', '', txt)  # "@~~"문자열 제거
            pattern = '(http|https)://(?:[-\w.]|(?:%[\da-zA-Z]{2}))+/[\da-zA-Z]+'  # URL제거
            txt = re.sub(pattern=pattern, repl='', string=txt)

            txt_list.append(txt)
            daily_list[int(day)].append(txt)
            hourly_list[int(hour)].append(txt)

# frequent word 구하기
for txt in txt_list:
    final_txt = txt.lower()
    stop_words = set(stopwords.words('English'))
    #tokenizer = RegexpTokenizer(r'\w+')
    tokenizer = RegexpTokenizer(r'[a-z]{3,}')       #3글자 이상의 영어단어만 허용
    word_tokens = tokenizer.tokenize(final_txt)
    filtered_sentence = [w for w in word_tokens if w not in stop_words]

    for w in filtered_sentence:
        if w not in final_dictionary:
            final_dictionary[w] = 1
        else:
            final_dictionary[w] = final_dictionary[w] + 1

sorted_d = sorted(final_dictionary.items(), key=operator.itemgetter(1), reverse=True)
freqWord = sorted_d[0:16]   #15개 까지만 추출

x_bar = []
y_bar = []
for i in freqWord:
    x_bar.append(i[0])
    y_bar.append(i[1])

plt.figure(figsize=(8, 8))

plt.title('Frequency of Most Frequent Words')
plt.xlabel('word')
plt.ylabel('frequency')
plt.xticks(rotation=45)

plt.bar(x_bar, y_bar, width=0.6, color='purple')
plt.show()


# 날짜 별 트윗 개수 보여주기
dailyCnt = []
for i in range(23,29):
    dailyCnt.append(len(daily_list[i]))

plt.figure(figsize=(8, 8))

plt.title('# of tweets per Day')
plt.xlabel('day')
plt.ylabel('# of tweets')

plt.bar(daily_list.keys(), dailyCnt, width=0.6, color='orange')
plt.show()


# 시간 별 트윗 개수 보여주기
hourlyCnt = []
for i in range(0,24):
    hourlyCnt.append(len(hourly_list[i]))

plt.figure(figsize=(8, 8))

plt.title('# of tweets per Hour')
plt.xlabel('hour')
plt.ylabel('# of tweets')

plt.bar(hourly_list.keys(), hourlyCnt, width=0.6, color='slateblue')
plt.show()


# 날짜 별 sentiment analysis
dictionary = {}
dictionary['positive'] = 0
dictionary['neutral'] = 0
dictionary['negative'] = 0

positive = []
neutral = []
negative =[]

for ii in daily_list.values():
    total_sentiment = 0
    for txt in ii:
        sentiment = TextBlob(txt).polarity  # 이 트윗 하나의 감정 수치

        if sentiment == 0:
            dictionary['neutral'] = dictionary['neutral'] + 1
        elif sentiment > 0:
            dictionary['positive'] = dictionary['positive'] + 1
        else:
            dictionary['negative'] = dictionary['negative'] + 1

    positive.append(dictionary['positive'])
    neutral.append(dictionary['neutral'])
    negative.append(dictionary['negative'])

ind = np.arange(6)
width = 0.5

p1 = plt.bar(ind, negative, width, color='red')
p2 = plt.bar(ind, neutral, width, bottom=negative, color='olive')
p3 = plt.bar(ind, positive, width, bottom=neutral, color='blue')

plt.ylabel('# of tweets per sentiment')
plt.xlabel('Day')
plt.title('Sentiment Analysis per Day')
plt.xticks(ind, ('23', '24', '25', '26', '27', '28'))
plt.legend((p1[0], p2[0], p3[0]), ('negative', 'neutral', 'positive'))

plt.show()

# 시간 별 sentiment analysis
dictionary['positive'] = 0
dictionary['neutral'] = 0
dictionary['negative'] = 0

positive = []
neutral = []
negative = []

for ii in hourly_list.values():
    total_sentiment = 0
    for txt in ii:
        sentiment = TextBlob(txt).polarity  # 이 트윗 하나의 감정 수치

        if sentiment == 0:
            dictionary['neutral'] = dictionary['neutral'] + 1
        elif sentiment > 0:
            dictionary['positive'] = dictionary['positive'] + 1
        else:
            dictionary['negative'] = dictionary['negative'] + 1

    positive.append(dictionary['positive'])
    neutral.append(dictionary['neutral'])
    negative.append(dictionary['negative'])

ind = np.arange(24)
width = 0.5

p1 = plt.bar(ind, negative, width, color='red')
p2 = plt.bar(ind, neutral, width, bottom=negative, color='olive')
p3 = plt.bar(ind, positive, width, bottom=neutral, color='blue')

plt.ylabel('# of tweets per sentiment')
plt.xlabel('Hour')
plt.title('Sentiment Analysis per Hour')
plt.xticks(ind, ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'))
plt.legend((p1[0], p2[0], p3[0]), ('negative', 'neutral', 'positive'))

plt.show()
