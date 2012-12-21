from QueryProcess import *
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
	print 'too few argument.'
    else:
        processer = QueryProcess()
	query_file = sys.argv[1]
	qf = open(query_file)
	rf = open('queryresult', 'w')

	for query in qf:
	    querylist = query.replace('\n', '').split(' ')
	    result = processer.query(querylist)
	    for (doc_name, doc_path, doc_size, doc_ct, word_size) in result[0:10]:
		rf.write('%s\t%s\t%s\n' % (doc_path, doc_size, time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(float(doc_ct)))))
	    rf.write('\n')

	qf.close()
	rf.close()
	    
    
    
