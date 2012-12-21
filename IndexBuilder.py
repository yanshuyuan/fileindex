import os
from Posting import *

class IndexBuilder(object):
    def __init__(self):
	pass	

    def build(self):
	doc_list = []
	for filename in os.listdir('.'):
	    if filename.startswith('.t'):
		doc_list.append(filename)
	
	filename = self.merge_sort(doc_list, 0, len(doc_list) - 1)
    	poster = Posting()
	poster.posting(filename)
	

    def merge_sort(self, doc_list, low, high): 
	if low < high:
	    mid = (low + high) / 2 
	    self.merge_sort(doc_list, low, mid)
	    self.merge_sort(doc_list, mid + 1, high)
	    return self.merge(doc_list, low, mid, high)

    def merge(self, doc_list, low, mid, high):
	left_filename = ''.join(doc_list[low : mid + 1])
	right_filename = ''.join(doc_list[mid + 1 : high + 1])
	all_filename = ''.join(doc_list[low : high + 1])
	left_doc = open(left_filename)
	right_doc = open(right_filename)
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
	f.close()
	return all_filename

if __name__ == '__main__':
    builder = IndexBuilder()
    builder.build()
	
		    
		
		
		
	

    
		
