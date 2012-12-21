
class Document(object):
    def __init__(self):
	self._docs = dict()
	self._doc_id = 1

    def add(self, doc_info):
	doc_id = self._doc_id
	self._doc_id = self._doc_id + 1
	self._docs[doc_id] = doc_info
	return doc_id

    def find(self, doc_id):
	if self._docs.has_key(doc_id):
	    return self._docs[doc_id]
	else:
	    return None

    def save(self, filename='Docdb'):
	f = open(filename, 'w')
	for doc_id in self._docs.keys():
	    (filename, fullpath, fsize, create_time, wsize) = self._docs[doc_id]
	    f.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (doc_id, filename, fullpath, fsize, create_time, wsize))
	f.close()
