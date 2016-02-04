from os.path import isdir as isdir
from os.path import isfile as isfile
from os.path import abspath as abspath
from os.path import join as joinPaths
from os import listdir as listdir
from os.path import basename


class NuGetScanner:

    @staticmethod
    def main():
        rootPath = abspath(".")
        Scanner.scan(rootPath)

class Scanner:
    @staticmethod
    def scan(path):
        for file in listdir(path):
            absolute = joinPaths(path,file)
            if isdir(absolute):
                Scanner.scan(absolute)
                #print (abspath(absolute))
            if isfile(absolute):
                filename = basename(absolute).lower()
                if ( filename.endswith('.csproj')):
                    print (filename)
                if (filename == 'packages.config'):
                    print (' * ' + absolute)


NuGetScanner.main()