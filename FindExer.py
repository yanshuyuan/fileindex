from Dictionary import *
from Document import *
from Reader import *
from Tokenizer import *
from Vocabulary import *
from IndexBuilder import *
import sys
import time


if __name__ == '__main__':
    if len(sys.argv) < 3:
	print 'argument too few, need arg(lexdb, rootdir)'
    else:
	lexdb, rootdir = sys.argv[1], sys.argv[2]
	
	print 'Reading Dictionary...'
        token = Tokenizer(Dictionary(lexdb))
        reader = Reader(rootdir)
        document = Document()
        vocabulary = Vocabulary()
        indexBuilder = IndexBuilder()
	i = 1
	print 'Parsing...'
        for (filename, fullpath, filesize, create_time) in reader.txt_files(): 
            print 'Process %d: %s' % (i, fullpath)
	    i += 1
            token_stream = token.parse(fullpath)
            doc_id = document.add((filename, fullpath, filesize, create_time, len(token_stream)))
            vocabulary.add(doc_id, token_stream)
	print 'Saving vocabulary...'
        vocabulary.save()
	print 'Saving document...'
        document.save()
	print 'Building index...'
        indexBuilder.build(vocabulary.files())
	print 'Over'
    
