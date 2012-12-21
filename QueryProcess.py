import time
class QueryProcess(object):
    def __init__(self, doc_file='Docdb', voc_file='Vocabulary'):
	self._doc = dict()
	self._voc = dict()
	self.__read_doc(doc_file)
	self.__read_voc(voc_file)

    def __read_doc(self, doc_file):
	f = open(doc_file)
	for doc_info in f:
	    try:
	        (doc_id, doc_name, doc_path, doc_size, doc_ct, word_size) = doc_info.replace('\n', '').split('\t')
	        self._doc[doc_id] = (doc_name, doc_path, doc_size, doc_ct, word_size)
	    except Exception, e:
		print doc_info
	f.close()

    def __read_voc(self, voc_file):
	f = open(voc_file)
	for voc_info in f: 
	    (token, tid, wf, df, offset) = voc_info.replace('\n', '').split('\t')
	    self._voc[token] = (tid, wf, df, offset)
	f.close()


    def query(self, querylist):
	pf = open('Posting')
	doc_ids = set()
	flag = False
	
	for word in querylist:
	    if self._voc.has_key(word):
		(tid, wf, df, offset) = self._voc[word]
		pf.seek(int(offset))
		posting = pf.readline().split('\t')[1].replace('\n', '').split(',')
		pset = set()
		for doc_id in posting:
		    pset.add(doc_id)
		if flag:
		    doc_ids.intersection_update(pset)
		else:
		    doc_ids = pset
		    flag = True
	pf.close()
	found_info = []
	for doc_id in doc_ids:
	    if self._doc.has_key(doc_id):
		found_info.append(self._doc[doc_id])
	return found_info
	

if __name__ == '__main__':
    import sys
    querylist = sys.argv[1:]
    print querylist
	
    process = QueryProcess()
    print process.query(querylist)
    
