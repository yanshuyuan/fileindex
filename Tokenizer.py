from Dictionary import *
from Reader import *

class Tokenizer(object):
    def __init__(self, Dict):
	self._word_dict = Dict

    def parse(self, filename):
	stream = {}
	fp = open(filename)
	
	new_word = ''
	word = ''
	
	for w in fp.read().decode('utf8'):
	    #print (word + w).encode('utf8')
	    new_word = word + w
	    while new_word:
		#print 'new: ', new_word.encode('utf8')
	        if not self._word_dict.find(new_word):
		    if word:
		        #print 'word: ', word.encode('utf8')
			if not stream.has_key(word):
			    stream[word] = 0
			stream[word] += 1
		        new_word = w
			word = ''
		    else:
			break
	        else:
		    #print 'find: ', new_word.encode('utf8')
		    word = new_word
		    break
	return stream
	
		
if __name__ == '__main__':
    token = Tokenizer(Dictionary('lexdb1.dat'))
    reader = Reader('.')
    for (filename, fullpath, filesize, create_time) in reader.txt_files(): 
	print filename
	stream = token.parse(fullpath)
	print len(stream)
	for key in stream.keys():
	    print '%s: %s' % (key, stream[key])
	print '-----------------------'
		     
	
		

