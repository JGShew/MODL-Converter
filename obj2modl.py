import struct
import sys
import os

objfile = open(sys.argv[1], "r")
objlines = objfile.readlines()

numvert = 0
numtexcoord = 0
numtri = 0
numtex = 0
texlist = []
texids = []

vertdat = []
texcoorddat = []
tridat = []

currtex = 0

for line in objlines:
    dat = line.split(" ")

    if dat[0] == "usemtl":
        if not(dat[1] in texlist):
            texlist.append(dat[1])
            numtex += 1
            currtex = numtex - 1
            theID = input("identifier for material '" + dat[1][:len(dat[1]) - 1] + "': ")
            texids.append(theID)
        else:
            currtex = texlist.index(dat[1])
    elif dat[0] == "v":
        numvert += 1
        vertdat.append(struct.pack(">f", float(dat[1])))
        vertdat.append(struct.pack(">f", float(dat[2])))
        vertdat.append(struct.pack(">f", float(dat[3])))
    elif dat[0] == "vt":
        numtexcoord += 1
        texcoorddat.append(struct.pack(">f", float(dat[1])))
        texcoorddat.append(struct.pack(">f", float(dat[2])))
    elif dat[0] == "f":
        numtri += 1
        v1 = dat[1].split("/")
        v2 = dat[2].split("/")
        v3 = dat[3].split("/")
        tridat.append(struct.pack(">I", int(v1[0])-1))
        tridat.append(struct.pack(">I", int(v2[0])-1))
        tridat.append(struct.pack(">I", int(v3[0])-1))
        tridat.append(struct.pack(">I", int(v1[1])-1))
        tridat.append(struct.pack(">I", int(v2[1])-1))
        tridat.append(struct.pack(">I", int(v3[1])-1))
        tridat.append(struct.pack(">I", currtex))

modlfile = open(sys.argv[2], "wb")
modlfile.write(b"\x4d\x4f\x44\x4c")
modlfile.write(struct.pack(">I", numvert))
modlfile.write(struct.pack(">I", numtexcoord))
modlfile.write(struct.pack(">I", numtri))
modlfile.write(struct.pack(">I", numtex))
for dat in vertdat:
    modlfile.write(dat)
for dat in texcoorddat:
    modlfile.write(dat)
for dat in tridat:
    modlfile.write(dat)
for theID in texids:
    modlfile.write(bytes(theID, encoding="ascii"))
    modlfile.write(b"\x00")
modlfile.close()

objfile.close()