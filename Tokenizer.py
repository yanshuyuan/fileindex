from Dictionary import *
from Reader import *
import time

class Tokenizer(object):
    def __init__(self, Dict):
	self._word_dict = Dict

    def parse(self, filename):
	stream = {}
	fp = open(filename)
	
	new_word = ''
	word = ''
	
	content = fp.read()
	charsets = ['utf8', 'utf16', 'utf32', 'gb18030', 'gbk', 'gb2312', \
		    'big5', 'big5hkscs', 'ascii', 'cp037', 'cp437', 'cp950', \
		    'hz', 'iso2022_jp_2']
	
	for charset in charsets:
	    try:
	        decode_content = content.decode(charset)
	    except Exception, e:
		continue
	    for w in decode_content:
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
	    break

	if not stream:
	    print 'File: %s unknown code' % filename
	return stream
	
		
if __name__ == '__main__':
    token = Tokenizer(Dictionary('lexdb.dat'))
    reader = Reader('.')
    for (filename, fullpath, filesize, create_time) in reader.txt_files(): 
	print filename
	stream = token.parse(fullpath)
	print len(stream)
	for key in stream.keys():
	    print '%s: %s' % (key, stream[key])
	print '-----------------------'
		     
	
		

