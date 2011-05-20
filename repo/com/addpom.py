import os, stat
import re
import shutil

reg = re.compile("\\\\(\w+?)\\\\((\d|\.)+)$")
def visit_dirs(dir):
	match = re.search(reg, dir)
	if match != None:
		version = match.group(2)
		name = 	match.group(1)	
		print ("%s %s" % (name, version))
		str = """
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ml</groupId>
    <artifactId>{name}</artifactId>
    <version>{version}</version>
    <packaging>jar</packaging>
</project>		
		""".format(name=name, version=version)
		print str
		file = open("%s\\%s-%s.pom" % (dir,name, version), "w")
		file.write(str)
		file.close()
		return		
	for f in os.listdir(dir):
		sub_dir = dir + "\\" + f
		if not os.path.isdir(sub_dir):
			continue		
		visit_dirs(sub_dir)
	
visit_dirs(".")