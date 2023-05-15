#coding:gbk
import re
import sys
import os
os.chdir(sys.argv[1])
for srcFile in os.listdir():
    if re.match('sn.._\.pst', srcFile):
        tmpFile=srcFile + ".tmp"
        fp_r=open(srcFile, "r", encoding='gbk', errors='ignore')
        fp_w=open(tmpFile, "w")
        for line in fp_r:
            if re.match('int\s+PlayerWeapon\s*=\s*.*;', line):
                line = "int PlayerWeapon = " + sys.argv[2] + ";\n"
            elif re.match('int\s+PlayerWeapon2\s*=\s*.*;', line):
                line = "int PlayerWeapon2 = " + sys.argv[3] + ";\n"
            fp_w.write(line)
        fp_r.close()
        fp_w.close()
        os.remove(srcFile)
        os.rename(tmpFile, srcFile)
