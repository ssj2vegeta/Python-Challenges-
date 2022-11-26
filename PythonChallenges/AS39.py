import random

allsongs = []
k = 1
for i in range(10):
    songs = ["a"+str(k),"b"+str(k), "c"+str(k), "d"+str(k), "e"+str(k), "f"+str(k), "g"+str(k), "h"+str(k), "i"+str(k), "j"+str(k)]
    allsongs.append(songs)
    k += 1
songstobeplayed = []
k = 0
while k < 20:
    temporarylist = []
    o = random.randint(0,9)
    d = allsongs[o]
    print(d)
    m = random.randint(0,9)
    try:
        l = d[m]
    except IndexError as e:
        print(f"{e}")
        continue
    if len(d) > 8:
        songstobeplayed.append(l)
        for i in allsongs:
            if l in i:
                i.remove(l)
        k += 1
        print(k)
    elif len(d) == 8:
        continue
print(songstobeplayed)
