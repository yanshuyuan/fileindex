import sys

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
	    pf.write('%s\t%s' % (tid, posting))
	    vf.write('%s\t%s\t%s\t%s\t%s\n' % (token, tid, wf, df, offset))
	    tid += 1
	vf.close()
	pf.close()
	fp.close()
	
if __name__ == '__main__':
    if len(sys.argv) < 2:
	print 'too few argument.'
    else:
        poster = Posting()
        poster.posting(sys.argv[1])
         
