with open('happiness_seg.txt',encoding='utf-8') as f:
	file = f.read()
	
import collections

filelist = file.split()
filelist1 = list()
for i in range(len(filelist) - 1):
	if (len(filelist[i]) > 1 and len(filelist[i+1]) > 1):
		filelist1.append(filelist[i] + " " + filelist[i+1])
		
frequency = collections.Counter(filelist1)

print (frequency.most_common(10))