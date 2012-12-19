import os
class Reader(object):
    def __init__(self, root_dir):
	self._root_dir = root_dir
 
    def __iter__(self):
	for item in os.walk(self._root_dir):
	    yield item

    def files(self):
	for (root, dirs, files) in self:
	    for filename in files:
		yield self.__file_info(root, filename)

    def dirs(self):
	for (root, dirs, files) in self:
	    for dirname in dirs:
		yield self.__file_info(root, dirname)

    def txt_files(self):
	for (filename, fullpath, filesize, create_time) in self.files():
	    if filename.endswith('.txt'):
		yield (filename, fullpath, filesize, create_time)

    def __file_info(self, root, filename):
	fullpath = os.path.join(root, filename)
	#(filename, fullpath, filesize, create_time)
	return (filename, fullpath, os.path.getsize(fullpath), os.path.getctime(fullpath))
	
	


if __name__ == '__main__':
    reader = Reader('.')
    print '---------------------------'
    for item in reader:
	print item

    print '---------------------------'
    for filename in reader.files():
	print filename

    print '---------------------------'
    for dirname in reader.dirs():
	print dirname

    print '---------------------------'
    for txtname in reader.txt_files():
	print txtname

	
