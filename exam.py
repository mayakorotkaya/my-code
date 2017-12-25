import os
import re
from flask import Flask
from flask import render_template, request, redirect, url_for
import json

def dict():
    files = os.listdir('/Users/mayakorotkaya/Desktop/thai_pages')
    html = filter(lambda x: x.endswith('.html'), files)
    for h in html:
        path='/Users/mayakorotkaya/Desktop/thai_pages/'+h
        with open (path, 'r', encoding='UTF-8') as source:
            source = source.read()
            #print(source)
            dicttaieng={}
            regeWordtai = re.compile("<td class=th><a href='.*?'>.*?</a></td>", flags=re.DOTALL)
            taiwords = regeWordtai.findall(source)
            regAll = re.compile('[a-zA-Z0-9_#;<>&/\№|=\{\}:\."\?\(\)\-@«»\']', re.DOTALL)
            regSpace = re.compile('\s+', re.DOTALL)
            new_taiwords=[]
            for i in taiwords:
                clean_i = regSpace.sub("", i)
                clean_i = regAll.sub("", clean_i)
                new_taiwords.append(clean_i)
            regeWordeng = re.compile("<span class='tt'>L</span></td><td class=pos>.*?</td><td>.*?</td>",
                                     flags=re.DOTALL)
            engwords = regeWordeng.findall(source)
            regAll1 = re.compile('[0-9_#;<>&/\№|=\{\}:\."\?\(\)\-@«»]', re.DOTALL)
            regHM = re.compile("span|class|tt|L|td|pos example sentence|pos noun|pos verb")
            regSpace1 = re.compile('\s+', re.DOTALL)
            new_engwords=[]
            for e in engwords:
                clean_e = regSpace1.sub(" ", e)
                clean_e = regAll1.sub(" ", clean_e)
                clean_e = regHM.sub("", clean_e)
                new_engwords.append(clean_e)

            for i in new_taiwords:
                dicttaieng[i]=new_engwords[new_taiwords.indexOf("i")]
            dictengtai={}
            for n in new_engwords:
                dictengtai[n]=new_taiwords[new_engwords.indexOf("n")]

            w = open('dicttieng.json', 'w', encoding='utf-8')
            json.dump(dicttaieng, w)
            w.close()
            z = open('dictengtai.json', 'w', encoding='utf-8')
            json.dump(dictengtai, z)
            z.close()

            return dicttaieng
app = Flask(__name__)

@app.route('/')
def index():
    if request.args:
        f = open('dictengtai.json', 'r', encoding='utf-8')
        dictengtai = json.load(f)
        f.close()
    #return render_template('vvedite.html')


print(dict())


