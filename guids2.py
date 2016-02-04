import uuid
import sys
def getGuids(count):
	f = open('pguids2result.txt','a')
	for x in range(1,count):
		f.writelines(str(uuid.uuid4())+'\n')
	f.close();
getGuids(int(sys.argv[1]));