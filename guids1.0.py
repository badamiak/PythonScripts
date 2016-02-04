import uuid
def getGuid(count):
	a = 0
	f = open('d:\guid_py.txt','w')
	while a < count
		f.write(uuid.uuid4() + '\n')
		a += 1
	f.flush()
	f.close()