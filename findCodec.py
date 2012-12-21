import sys
c = open('charset')
charsets = []
for ch in c:
    charsets.append(ch.replace('\n', ''))
c.close()

filename = sys.argv[1]
if filename.endswith('.TXT') or filename.endswith('.txt'):
    fp = open(filename)
    s = fp.read()
    for char in charsets:
        try:
            s.decode(char)
        except Exception, e:
            continue
	print char
        break
    fp.close()
       
