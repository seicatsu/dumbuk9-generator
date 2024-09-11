import time
import random

name = ["d", "ü", "m", "b", "ü", "k"]
sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
sessiz = ["z", "y", "v", "t", "ş", "s", "r", "p", "n", "r", "m", "l", "k", "h", "j", "ğ", "g", "d", "ç", "c", "b"]
randomname =  ["d", "ü", "m", "b", "ü", "k"]
random.shuffle(randomname)
print(randomname)
def dumbuki():
    num = 0
    random.shuffle(randomname)
    for letter in randomname:
        if letter in sesli:
            name[name.index(letter)] = random.choice(sesli)
            num += 1
        elif letter in sessiz:
            name[name.index(letter)] = random.choice(sessiz)
            num +=1
        if num >= 3:
            return
print(name)
while True:
        time.sleep(0.5)
        dumbuki()
        isim = ''.join(name)
        print(isim +"9")
        name = ["d", "ü", "m", "b", "ü", "k"]


print(name)

