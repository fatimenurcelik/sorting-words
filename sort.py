fname = input("Enter file name: ")
fh = open(fname,"r")
lines=fh.readlines()
kelimeler=list()
for line in lines:
    x=line.split()
    for kelime in x:
        if not kelime in kelimeler:
            kelimeler.append(kelime)
kelimeler.sort()
print(kelimeler)
