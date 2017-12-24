import sqlite3

conn = sqlite3.connect('hittite.db')
c = conn.cursor()

c.executescript('''DROP TABLE IF EXISTS words;
CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY AUTOINCREMENT, lemma TEXT, wordform TEXT, glosses TEXT)''')
c.execute('INSERT INTO words (lemma, wordform, glosses) SELECT lemma, wordform, glosses FROM wordforms')
glossa_id={}
for g in c.execute('SELECT id, glosses FROM words'):
    id, gloss = g[0], g[1]
    gloss = gloss.split('.')
    gloss = ' '.join(gloss)
    glossa_id[id] = gloss
sort=sorted(glossa_id)
for s in sort:
    c.execute('UPDATE words SET glosses = ? WHERE id = ? ', [glossa_id[s], s])
with open ('glosses.txt', 'r', encoding='utf-8') as f:
    glosses = f.read()
    glosses = glosses.split('\n')
i = 0
newglosses = []
for g in glosses:
    i+=1
    g = g.split(' — ')
    go = []
    go.append(str(i))
    go.append(g[0])
    go.append(g[1])
    newglosses.append(go)
#print(newglosses)
c.executescript('''DROP TABLE IF EXISTS meaning_of_glossa;
CREATE TABLE IF NOT EXISTS meaning_of_glossa (id INTEGER PRIMARY KEY AUTOINCREMENT, glossa TEXT, meaning TEXT)''')
for z in newglosses:
    c.execute('''INSERT INTO meaning_of_glossa VALUES (?, ?, ?)''', [z[0], z[1], z[2]])
glossa_i_slovo = {}
c.execute('SELECT id, glossa FROM meaning_of_glossa ORDER BY id')
r=c.fetchall()
for g in r:
    id_glossa = g[0]
    glossa = g[1]
    #print(glossa)
    c.execute('SELECT id, glosses FROM words WHERE glosses LIKE ? ', (glossa,))
    b = c.fetchall()
    for f in b:
        id_word = f[0]
        #print(id_word)
        id_word = str(id_word)
        for i in id_word:
            glossa_i_slovo[id_glossa] = i
#print(glossa_i_slovo)

# c.execute('SELECT glossa FROM meaning_of_glossa')
# gls=c.fetchall()
#
# gl_to_words=[]
# glnum=0
# for glsitem in gls:
#     glnum+=1
#     glsitem=glsitem[0]
#     #print(glsitem)
#     c.execute('SELECT id, glosses FROM words WHERE glosses LIKE ? ', (glsitem,))
#     b=c.fetchall()
#     #print(b)
#     bgood=[]
#     for bpair in b:
#         fortup=[bpair[0], glnum]
#         bgood.append(tuple(fortup))
#         gl_to_words.append(tuple(fortup))
# print(gl_to_words)
c.executescript('''DROP TABLE IF EXISTS ids; CREATE TABLE IF NOT EXISTS ids (id_word INTEGER, id_glossa INTEGER)''')
for h in glossa_i_slovo:
    c.execute('''INSERT INTO ids VALUES (?, ?)''', [glossa_i_slovo[h], h])
#for gl in gl_to_words:
#    c.execute('INSERT INTO ids VALUES (? , ?) ', [gl[0], gl[1]])

#c.execute('SELECT id FROM meaning_of_glossa JOIN ids ON id = id_glossa')
conn.commit()

##cur.execute('SELECT * FROM arcitles')
##rows = cur.fetchall()
##
##for row in rows:
##    print(row)

#заносим еще чето в базу данных
# title = input("title: ")
# url = input("url: ")
#
# cur.execute('INSERT INTO  articles (title, url) VALUES (?, ?)', [title, url])
#conn.commit()
