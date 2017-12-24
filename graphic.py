import sqlite3
import matplotlib.pyplot as plt

conn=sqlite3.connect('hittite.db')
c=conn.cursor()
c.execute('SELECT glosses FROM words')
glosses = c.fetchall()
dictpronglosses={}
dictconjglosses={}
dictsubglosses={}
dictverbglosses={}
for g in glosses:
    glossa = g[0].split(' ')
    if "PRON" in glossa:
        for o in glossa:
            if o!="PRON" and o.lower() != o:
                if o not in dictpronglosses:
                    dictpronglosses[o]=1
                else:
                    dictpronglosses[o]+=1
    elif "CONJ" in glossa:
        for k in glossa:
            if k!="CONJ" and k.lower() != k:
                if k not in dictconjglosses:
                    dictconjglosses[k]=1
                else:
                    dictconjglosses[k]+=1
    elif "LOC" in glossa:
        for l in glossa:
            if l!="LOC" and l.lower() != l:
                if l not in dictsubglosses:
                    dictsubglosses[l]=1
                else:
                    dictsubglosses[l]+=1
    elif "PST" in glossa or "PRS" in glossa or "PRT" in glossa or "IMF" in glossa:
        for m in glossa:
            if m.lower() !=m:
                if m not in dictverbglosses:
                    dictverbglosses[m]=1
                else:
                    dictverbglosses[m]+=1
verbx=[]
verby=[]
for verbglossa in sorted(dictverbglosses):
    verbx.append(verbglossa)
    verby.append(dictverbglosses[verbglossa])
verbxaxis=[a for a in range(1, len(verbx)+1)]
plt.title('Verb glosses')
plt.xlabel('Glossa')
plt.ylabel('Number of tokens')
for x, y, gl in zip(verbxaxis, verby, verbx):
    plt.bar(x, y)
    plt.text(x-0.5, y+0.2, gl)
plt.show()
conjitems=[]
conjy=[]
for conjglossa in sorted(dictconjglosses):
    conjitems.append(conjglossa)
    conjy.append(dictconjglosses[conjglossa])
conjx=[c for c in range(1, len(conjitems)+1)]
plt.title('Conj glosses')
plt.xlabel('Glossa')
plt.ylabel('Number of tokens')
for x, y, gl in zip(conjx,conjy,conjitems):
    plt.bar(x,y)
    plt.text(x-0.5, y+0.2, gl)
plt.show()
pronitems=[]
prony=[]
for pronglossa in sorted(dictpronglosses):
    pronitems.append(pronglossa)
    prony.append(dictpronglosses[pronglossa])
pronx=[b for b in range(1, len(pronitems)+1)]
plt.title('Pronoun glosses')
plt.xlabel('Glossa')
plt.ylabel('Number of tokens')
for x, y, gl in zip(pronx,prony,pronitems):
    plt.bar(x,y)
    plt.text(x-0.5, y+0.2, gl)
plt.show()
subitems=[]
suby=[]
for subglossa in sorted(dictsubglosses):
    subitems.append(subglossa)
    suby.append(dictsubglosses[subglossa])
subx=[b for b in range(1, len(subitems)+1)]
plt.title('Noun glosses')
plt.xlabel('Glossa')
plt.ylabel('Number of tokens')
for x, y, gl in zip(subx,suby,subitems):
    plt.bar(x,y)
    plt.text(x-0.5, y+0.2, gl)
plt.show()