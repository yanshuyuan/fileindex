from Dictionary import *
from Document import *
from Reader import *
from Tokenizer import *
from Vocabulary import *
from IndexBuilder import *


if __name__ == '__main__':
    token = Tokenizer(Dictionary('lexdb.dat'))
    reader = Reader('.')
    document = Document()
    vocabulary = Vocabulary()
    indexBuilder = IndexBuilder()
    for (filename, fullpath, filesize, create_time) in reader.txt_files(): 
	print 'Process: %s' % fullpath
	token_stream = token.parse(fullpath)
	doc_id = document.add((filename, fullpath, filesize, create_time, len(token_stream)))
	vocabulary.add(doc_id, token_stream)
    vocabulary.save()
    document.save()
    indexBuilder.build(vocabulary.files())
		     
	
	
    
