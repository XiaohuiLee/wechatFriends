# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import itchat
itchat.auto_login()


friends = itchat.get_friends(update = True)[0:]
male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

        total = len(friends[1:])


print (u"男性好友：%.2f%%" % (float(male) / total * 100))
print (u"女性好友：%.2f%%" % (float(female) / total * 100))
print (u"其他：%.2f%%" % (float(other) / total * 100))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable
nickName = get_var('NickName')
sex = get_var("Sex")
province = get_var('Province')
city = get_var('City')
signature = get_var("Signature")
import sys
reload(sys)
sys.setdefaultencoding('utf8')


data = {
   "nickName" : nickName,
    "sex" : sex,
    "province" : province,
    "city" : city,
    "signature" : signature
}
df = pd.DataFrame(data)
df.to_csv("data.csv", index = True, encoding="utf_8_sig")


import re
siglist = []
for i in friends:
    sig = i['Signature'].strip().replace('span','').replace('class','').replace('emoji','')

    rep = re.compile("1f\d + \w*|[<>=/]")
    sig = re.sub(rep,"", sig)
    siglist.append(sig)
text = "".join(siglist)
print siglist
print text


import jieba
wordlist = jieba.cut(text, cut_all = True)
word_space_split = "".join(wordlist)


import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as image
coloring = np.array(image.open("D:/Wallpaper/bg.jpg"))
mywordCloud = WordCloud(background_color="white",
                       max_words = 2000,
                       mask = coloring,
                       max_font_size = 60,
                       random_state = 42,
                       scale = 2,
                        font_path = "LiheiPro.ttf"
                       ).generate(word_space_split)

imageColors = ImageColorGenerator(coloring)
plt.imshow(mywordCloud.recolor(color_func=imageColors))
plt.imshow(mywordCloud)
plt.axis("off")
plt.show()
import os
mywordCloud.to_file(os.path.join("cloud.png"))
