from Dictionary import *
from Document import *
from Reader import *
from Tokenizer import *
from Vocabulary import *


if __name__ == '__main__':
    token = Tokenizer(Dictionary('lexdb1.dat'))
    reader = Reader('.')
    document = Document()
    vocabulary = Vacabulary()
    for (filename, fullpath, filesize, create_time) in reader.txt_files(): 
	token_stream = token.parse(fullpath)
	doc_id = document.add((filename, fullpath, filesize, create_time, len(token_stream))
	vocabulary.add(doc_id, token_stream)
	
	for key in token_stream.keys():
	    print '%s: %s' % (key, token_stream[key])
	print '-----------------------'
    vocabulary.save()
    document.save()
		     
	
	
    
