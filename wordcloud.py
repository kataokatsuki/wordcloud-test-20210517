#!/usr/bin/env python3
import MeCab
from matplotlib import pyplot as plt
from wordcloud import WordCloud

with open('test.txt', encoding='utf-8') as f:
  read_data = f.read()

mecab = MeCab.Tagger("-Owakati")
tokenized_text = mecab.parse(read_data)

node = mecab.parseToNode(tokenized_text)
keywords = []
while node:
  if node.feature.split(",")[0] == u"名詞":
      keywords.append(node.surface)
  elif node.feature.split(",")[0] == u"形容詞":
      keywords.append(node.feature.split(",")[6])
  elif node.feature.split(",")[0] == u"動詞":
      keywords.append(node.feature.split(",")[6])
  node = node.next

string_keywords=(" ").join(keywords)

stop_words = [  
                u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', u'ます', u'です', u'から', u'思い', "できる", \
                u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
                u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
                u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u''
              ]

word_cloud = WordCloud(font_path='/System/Library/Fonts/ヒラギノ明朝 ProN.ttc', stopwords=set(stop_words), width=1000, height=1000).generate(string_keywords)
plt.imshow(word_cloud)
plt.axis('off')
plt.show()