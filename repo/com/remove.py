print "hello world"
print "hello world"
import os, stat
import shutil

def remove(dir, all_inside=False):
	if dir.endswith(".svn"):
		print dir
		os.chmod(dir, stat.S_IWRITE)  
		shutil.rmtree(dir)
		return		
	for f in os.listdir(dir):
		sub_dir = dir + "\\" + f
		if not os.path.isdir(sub_dir):
			continue		
		remove(sub_dir)
		
		
remove(".")		