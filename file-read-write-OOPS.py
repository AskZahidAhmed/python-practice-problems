import re
import sys

class File:
    def __init__(self, readFilename : str, writeFilename:str) -> str:
        self.readFilename = readFilename
        self.writeFilename = writeFilename
        self.lines = [] 

    def readFile(self)-> list[str]:
        with open(self.readFilename, 'r', encoding='utf-8') as f:
            self.lines = [line.strip() for line in f.readlines()]
        return self.lines

    def readLinesClean(self) -> list[str]:
        cleaned_lines = []
        for line in self.lines:
            line = re.sub(r'([\.\-\+\!\|\?\,\"\'\:\;])', r' \1 ', line)
            cleaned_line = re.sub(r'\s+', r' ', line)
            cleaned_lines.append(cleaned_line)
        return cleaned_lines
    
    def writeFile(self) -> None:
        cleaned_lines = self.readLinesClean()
        with open(self.writeFilename, 'w', encoding='utf-8') as f:
            for line in cleaned_lines:
                f.write(line + '\n')

    def printContent(self):
        pass

file_handler = File(sys.argv[1], sys.argv[2])
lines = file_handler.readFile()
cleaned_lines = file_handler.readLinesClean()
file_handler.writeFile()
