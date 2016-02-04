import uuid
def getGuids(count,path):
	f = open(path,'w')
	for x in range(1,count):
		f.write(str(uuid.uuid4())+'\n')
	f.close()