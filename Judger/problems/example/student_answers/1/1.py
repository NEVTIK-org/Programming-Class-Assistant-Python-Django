import os
import re
from urllib.parse import quote
from urllib.parse import unquote
import shutil
import sys
try:
 target = sys.argv[1]
 target_dir = os.path.basename(target).rstrip(".xspf")
except Exception:
 print("XSPF Extractor by KevinAS28. please specify xspf file as argument. example: python extractxspf.py mylist.xspf")
 sys.exit(0)
if (not os.access(target_dir, os.W_OK)):
 os.mkdir(target_dir)
daftar = []
with open(target, "r") as baca:
 data = baca.read().split("\n")
for i in data:
 if (re.match(r"(\s*)<location>(.*)</location>", i)):
  daftar.append(i.replace("<location>", "").replace("</location>", "").replace("&#39;", "'").strip("\t").replace("file://", ""))


failed=[]
def copy(src, dest):
 global failed
 try:
		open(dest, "w+")
		with open(src, "rb") as baca:
			with open(dest, "wb") as tulis:
				tulis.write(baca.read())
 except FileNotFoundError as a:
  failed.append(src)

for i in daftar:
 i = unquote(i)
 dest = os.path.join(target_dir, os.path.basename(i))
 print("Copying %s to %s\n\n" %(i, dest))
 copy(i, dest)

print("Total: %d"%(len(daftar)))
print("Fail: %s"%(str(failed)))
