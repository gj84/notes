import os, re, os.path

path = ""
subpath = "renamed"

lista = os.listdir(path)

regex = re.compile('\([0-9]+-[0-9]+\)')

for f in lista:
    oldpath = os.path.join(path, f)
    if f.split('.')[-1] == "mp4":
        n = re.search(regex,f).group(0).split('(')[1].split('-')[0]
        fname = f.split('(')[0]
        fname = fname[0:-1]
        if len(n) == 1:
            n = "0" + n
        newname = n+'-'+fname+'.mp4'
        newpath = os.path.join(path, subpath, newname)

        print(oldpath)
        print(newpath)
        try:
            os.rename(oldpath, newpath)
        except Exception as e:
            print(oldpath)
            print(e)
        print("------------------------\n")
		
