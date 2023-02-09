import collections
frasa = open('input_s1_09.txt').readline().split()
res = [] ; itog = []
for s in frasa:
    new = s[len(s)//2]
    for i in range(1, len(s)//2+len(s)%2):
        new += s[len(s)//2 - i] + s[len(s)//2+i]
    if len(s)%2 == 0: new += s[0]
    res.append(new)
itog.append(res[len(res)//2])
# print(res)
for i in range(1,len(res)//2 + len(res)%2):
    itog.append(res[len(res)//2-i])
    itog.append(res[len(res)//2+i])
if len(res)%2 == 0: itog.append(res[0])
# print(itog)
otvet = open('output_s1_09.txt').readline().split()
# print('Ответ:',otvet)
if collections.Counter(itog) == collections.Counter(otvet):
    print('Верно!')