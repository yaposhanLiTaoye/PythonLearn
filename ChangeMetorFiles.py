#coding:gbk
import re
import sys
import os
def ChangeFile(srcFile, pw1, pw2):
    tmpFile=srcFile + ".tmp"
    fp_r=open(srcFile, "r", encoding='gbk', errors='ignore')
    fp_w=open(tmpFile, "w")
    
    line = fp_r.readline()
    while line:
        if re.match('int\s+PlayerWeapon\s*=\s*.*;', line):
            print(line)
            fp_w.write("int PlayerWeapon = " + pw1 + ";\n")
        elif re.match('int\s+PlayerWeapon2\s*=\s*.*;', line):
            print(line)
            fp_w.write("int PlayerWeapon2 = " + pw2 + ";\n")
        else:
            fp_w.write(line)
        line = fp_r.readline()

    fp_r.close()
    fp_w.close()
    os.remove(srcFile)
    os.rename(tmpFile, srcFile)


if __name__ == "__main__":
    os.chdir(sys.argv[1])
    for file in os.listdir():
        if re.match('sn.._\.pst', file):
            ChangeFile(file, sys.argv[2], sys.argv[3])
