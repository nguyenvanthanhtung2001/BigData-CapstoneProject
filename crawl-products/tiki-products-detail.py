import os
import json
import codecs


with open("output/1.txt", "r", encoding="utf-8-sig") as f:
	lines = f.readlines()
	for line in lines:
		if len(line.strip()) == 0:
			continue
		a = json.loads(line, )
		print(a)
		break