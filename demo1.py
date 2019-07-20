data = 'yarn'
with open('network/dict.txt','r') as f:
    for  line in f.readlines():
        l = line.split()
        # l.remove(l[0])
        # s = ' '.join(l)
        # print(s)
        if data==l[0]:
            l.remove(l[0])
            s = ' '.join(l)
            print(s)
