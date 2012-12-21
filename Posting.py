class Posting(object):
    def __init__(self):
	pass

    def posting(self, filename):
	fp = open(filename)
	vf = open('Vocabulary', 'w')
	pf = open('Posting', 'w')
	tid = 0
	for line in fp:
	    (token, wf, df, posting) = line.split(' ')
	    offset = pf.tell()
	    pf.write('%s %s' % (tid, posting))
	    vf.write('%s %s %s %s %s\n' % (token, tid, wf, df, offset))
	    tid += 1
	vf.close()
	pf.close()
	fp.close()
	
         
