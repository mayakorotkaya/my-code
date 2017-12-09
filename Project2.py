from flask import Flask
from flask import render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    if request.args:
        f = open('data.json', 'r', encoding='utf-8')
        massive = json.load(f)
        f.close()
        dict = {'language': request.args['language'], 'answer1': request.args['answer1'], 'answer2': request.args['answer2']}
        massive.append(dict)
        w = open('data.json', 'w', encoding='utf-8')
        json.dump(massive, w)
        w.close()
    return render_template('anketa1.html')

@app.route('/json')
def json_file():
    f = open('data.json', 'r', encoding='utf-8')
    slovar=json.load(f)
    f.close()
    return render_template('answer2.html', dictionary=slovar)

@app.route('/stats')
def stats():
    z = open('data.json', 'r', encoding='utf-8')
    slovar = []
    sh = 0
    pl = 0
    ko = 0
    ka = 0
    for elem in json.load(z):
        slovar.append(elem['answer1'])
        slovar.append(elem['answer2'])
    for i in slovar:
        if i == 'шарф':
            sh += 1
        if i == 'платок':
            pl += 1
        if i == 'косынка':
            ko += 1
        if i == 'кашне':
            ka += 1
    all_answers = sh + pl
    z.close()
    return render_template('answer.html', sharf=sh, platok=pl, kosinka=ko, kashne=ka, all_answers=all_answers)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/result')
def result():
    z = open('data.json', 'r', encoding='utf-8')
    slovar = []
    sh = 0
    pl = 0
    ko = 0
    ka = 0
    word = 0
    people = 0
    for elem in json.load(z):
        slovar.append(elem['answer1'])
        slovar.append(elem['answer2'])
    for i in slovar:
        if i == 'шарф':
            sh += 1
        if i == 'платок':
            pl += 1
        if i == 'косынка':
            ko += 1
        if i == 'кашне':
            ka += 1
    if request.args:
        word = request.args['word']
        if word == 'шарф':
            people = sh
        if word == 'платок':
            people = pl
        if word == 'косынка':
            people = ko
        if word == 'кашне':
            people = ka
    z.close()
    return render_template('result.html', people=people, word=word)

if __name__ == '__main__':
    app.run(debug=True)