import os

catalogmaindir = "img/catalog"
catalogdirs = [os.path.join(catalogmaindir, f) for f in os.listdir(catalogmaindir)]
catalogimg = dict()
for catalogdir in catalogdirs:
    print(catalogdir.split(os.sep)[-1])
    catalogimg[catalogdir.split(os.sep)[-1]] = [os.path.join(catalogdir, f) for f in os.listdir(catalogdir)]

current_catalogimg = [None, None]
for el in catalogimg.keys():
    current_catalogimg += catalogimg[el]
current_catalogimg += [None, None]
print(current_catalogimg)