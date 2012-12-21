import time
class Vocabulary(object):
    def __init__(self):
	self._voc = {}
	self._voc_size = 0
	self._tmp_id = 0
	self.DEFAULT = 100000
	self._tmp_filename = []

    def reset(self):
	self._voc = {}
	self._voc_size = 0
	

    def add(self, doc_id, token_stream):
	for token in token_stream.keys():
	    if not self._voc.has_key(token):
		#(wf, df, doc_id_list)
		self._voc[token] = [0, 0, []]
		self._voc_size += 1
	    self._voc[token][0] += token_stream[token]
	    self._voc[token][1] += 1
	    self._voc[token][2].append('%s:%s' % (doc_id, token_stream[token]))
	if self._voc_size > self.DEFAULT:
	    self.save()
	    self.reset()

    def save(self):
	if self._voc:
	    f = open('.t' + str(self._tmp_id), 'w')
	    self._tmp_filename.append('.t' + str(self._tmp_id))
	    self._tmp_id += 1
	    for token in sorted(self._voc.keys()):
	        (wf, df, doc_info_list) = self._voc[token]
	        f.write('%s %s %s %s\n' % (token.encode('utf8'), wf, df, \
			reduce(lambda x,y: '%s,%s' % (x, y), doc_info_list)))
	    f.close()

    def files(self):
	return self._tmp_filename
	    
	
	
	


    
