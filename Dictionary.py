class Dictionary(object):
    def __init__(self, filename):
        self._word_dict = dict()
	self._filename = filename
	self.__read__()
   
    def __read__(self):
	fp = open(self._filename)
	for line in fp:
	    word = line.split(' ')[1].replace('\n', '').decode('gbk')
	    p = self._word_dict
	    for w in word:
		if not p.has_key(w):
		    p[w] = {}
		p = p[w]

	fp.close()

    def find(self, word):
	p = self._word_dict
	for w in word:
	    if p.has_key(w):
		p = p[w]
	    else:
		return False
	return True
	    


if __name__ == '__main__':
    def traverse(d, s):
	if d:
	    for key in d.keys():
	        traverse(d[key], s + key)
	else:
	    print s.encode('utf8')
		
	    
    d = Dictionary("lexdb.dat")
    traverse(d._word_dict, '')
	
	
	
