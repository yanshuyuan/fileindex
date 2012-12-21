
class QueryProcess(object):
    def __init__(self):
	pass

    def query(self, querylist):
	vf = open('Vocabulary')
	pf = open('Posting')
	res = set()
	flag = False
	
	for line in vf:
	    (token, tid, wf, df, offset) = line.split(' ')
	    if token in querylist:
		pf.seek(int(offset))
		posting = pf.readline().split(' ')[1].replace('\n', '').split(',')
		pset = set()
		for doc_id in posting:
		    pset.add(doc_id)
		if flag:
		    res.intersection_update(pset)
		else:
		    res = pset
		    flag = True
	vf.close()
	pf.close()
	return res
	

if __name__ == '__main__':
    import sys
    querylist = sys.argv[1:]
    print querylist
	
    process = QueryProcess()
    print process.query(querylist)
    
