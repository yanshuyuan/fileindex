class Vocabulary(object):
    def __init__(self):
	self._voc = {}
	self._voc_size = 0
	self._tmp_id = 0
	self.DEFAULT = 10000
	self._tmp_filename = []

    def reset(self):
	self._voc = {}
	self._voc_size = 0
	

    def add(self, doc_id, token_stream):
	for token in token_stream.keys():
	    if not self._voc.has_key(token):
		#(wf, df, doc_id_list)
		self._voc[token] = (0, 0, [])
		self._voc_size++;
	    self._voc[token][0] += token_stream[token]
	    self._voc[token][1] += 1
	    self._voc[token][2].append(doc_id)
	if self._voc_size > self.DEFAULT:
	    self.save()
	    self.reset()

    def save(self):
	f = open('.t' + str(self._tmp_id), 'w')
	self._temp_filename.append('.t' + str(self._tmp_id))
	self._tmp_id += 1
	for token in self._voc.keys().sort():
	    (wf, df, doc_id_list) = self._voc[token]
	    fwrite('%s %s %s %s\n' % (token, wf, df, ','.join(doc_id_list)))
	f.close()

    def files(self):
	return self._tmp_filename
	    
	
	
	


    
