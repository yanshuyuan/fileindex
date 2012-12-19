class Dictionary(object):
    def __init__(self, filename):
        self._word_dict = set()
	self._filename = filename
	self.__read__()

    def __iter__(self):
	for word in self._word_dict:
	    yield word
   
    def __read__(self):
	fp = open(self._filename)
	for line in fp:
	    word = line.split(' ')[1].decode('gbk')
	    if word:
	        self._word_dict.add(word[:len(word) - 1])
	fp.close()

    def find(self, word):
	return word in self._word_dict


if __name__ == '__main__':
    d = Dictionary("lexdb.txt")
    for word in d:
	print word
	
