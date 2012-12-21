import os
from Posting import *

class IndexBuilder(object):
    def __init__(self):
	self._merge_id = 0

    def build(self, doc_list):
	if len(doc_list) > 1:
	    filename = self.merge_sort(doc_list, 0, len(doc_list) - 1)
	else:
	    filename = ','.join(doc_list[:])
	
    	poster = Posting()
	poster.posting(filename)
	

    def merge_sort(self, doc_list, low, high): 
	if low < high:
	    mid = (low + high) / 2 
	    left_filename = self.merge_sort(doc_list, low, mid)
	    right_filename = self.merge_sort(doc_list, mid + 1, high)
	    all_filename =  self.merge(doc_list, low, mid, high, left_filename, right_filename)
	
	    return all_filename
	else:
	    return ','.join(doc_list[low : high + 1])

    def merge(self, doc_list, low, mid, high, left_filename, right_filename):
	left_doc = open(left_filename)
	right_doc = open(right_filename)
	all_filename = '.tmp%s' % (self._merge_id)
	self._merge_id += 1
	f = open(all_filename, 'w')
	l = left_doc.readline()
	r = right_doc.readline()
	ls = l.split(' ')
	rs = r.split(' ')
	while True:
	    if l and r:
		if ls[0] < rs[0]:
		    f.write(l)
		    l = left_doc.readline()
		    ls = l.split(' ')
		elif ls[0] == rs[0]:
		    m = '%s %s %s %s,%s\n' % (ls[0], int(ls[1]) + int(rs[1]), int(ls[2]) + int(rs[2]), ls[3].replace('\n', ''), rs[3].replace('\n', ''))
		    f.write(m)
		    l = left_doc.readline()
		    r = right_doc.readline()
		    ls = l.split(' ')
		    rs = r.split(' ')
		else:
		    f.write(r)
		    r = right_doc.readline()
		    rs = r.split(' ')
	    elif not l and not r: 
		break
	    elif l and not r:
		l = left_doc.readline() 
		f.write(l)
	    elif not l and r:
		r = right_doc.readline()
		f.write(r)
	left_doc.close()
	right_doc.close()
	f.flush()
	f.close()
	cmd = 'rm %s %s' % (left_filename, right_filename)
	os.system(cmd)
	
	return all_filename

if __name__ == '__main__':
    doc_list = []
    for filename in os.listdir('.'):
	if filename.startswith('.t') and (not filename.startswith('.tmp')):
	    doc_list.append(filename)
    print doc_list
 
    builder = IndexBuilder()
    builder.build(doc_list)
	
		    
		
		
		
	

    
		
