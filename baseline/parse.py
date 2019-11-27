import  re
parsed_doc = []
rel_indice = []
pattern = re.compile(r'\d+')
"""with open('ennso_parallel.test.en', 'r') as f:
    for row in f:
        m = pattern.findall(row)
        n = re.sub(pattern, "*", row)
        parsed_doc.append(n)
        rel_indice.append(','.join(m))

with open('ennso_parallel.test.en.new.txt', 'w') as w:
    w.write("".join(parsed_doc))
with open("rel.en.test.txt", 'w') as w:
    w.write("\n".join(rel_indice))"""
nso = []
en = []
from collections import Counter
cnt_en = Counter()
with open("jw300.en", 'r') as a, open("jw300.nso", 'r') as b:
    for row in zip(a, b):
        #print(row)

        x, y = row
        #print(len(x),len(y))
        x1 = x.split()
        cnt_en.update(x1)
        y1 = y.split()
        if len(x1) > 256 or len(y1) > 256: continue
        if bool(re.search(r'\d', x)) or bool(re.search(r'\d', y)): continue
        if len(x1) == 0 or len(y1) == 0: continue
        if "*" in x or "*" in y: continue
        #if "Amendment" in x: print('o')
        en.append(x)
        nso.append(y)
    print(sorted(cnt_en, key=lambda x: cnt_en[x], reverse=True)[:100])
with open("jw.en", 'w') as a, open("jw.neo", 'w') as b:
    a.write("".join(en))
    b.write("".join(nso))
