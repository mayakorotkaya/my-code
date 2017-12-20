from flask import Flask
from flask import url_for, render_template, request
import urllib.request
import re

def info(page):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request(page, headers={'User-Agent': user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        regeWord = re.compile('<td class="uu">.*?</td>', flags=re.DOTALL)
        words = regeWord.findall(html)
        #goodword = words.group(1)
    regAll = re.compile('[a-zA-Z0-9_#;&/\№|=\{\}:\."\?\(\)\-@«»]', re.DOTALL)
    regSpace = re.compile('\s+', re.DOTALL)
    new_words=[]
    for i in words:
        clean_i = regSpace.sub("", i)
        clean_i = regAll.sub("", clean_i)
        new_words.append(clean_i)
    return new_words



app = Flask(__name__)

@app.route('/')
def index():
    urls = {'главная (эта страница)': url_for('index'),'страница с формой': url_for('form'), 'страница с извинениями': url_for('sorry')}
    return render_template('links.html', urls=urls)

@app.route('/form')
def form():
    if request.args:
        word = request.args['word']
        #дальше попытка извлеченному из ссылки слову подобрать значение из дореволюционного словаря
        commonUrl = 'http://www.dorev.ru/ru-index.html?l=c'
        new_words = []
        for i in range(0, 9):
            pageurl = commonUrl + str(i)
            new_words.append(info(pageurl))
        for elem in new_words:
            if word in elem:
                word = new_words[new_words.indexOf("word") + 1]
            else:
                word = "В словаре нет такого слова, а сделать с этим что-то я не успела :("

        return render_template('slovo.html', word=word)
    return render_template('question.html')

@app.route('/sorry')
def sorry():
    return render_template('sorry.html')

if __name__ == '__main__':
    app.run(debug=True)
