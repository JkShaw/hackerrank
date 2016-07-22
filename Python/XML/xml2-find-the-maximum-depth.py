# Enter your code here. Read input from STDIN. Print output to STDOUT
from xml.etree.ElementTree import XMLParser

class MaxDepth:
    maxDepth = 0
    depth = 0
    
    def start(self, tag, attrib):
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
    
    def end(self, tag):
        self.depth -= 1
    
    def data(self, data):
        pass
    
    def close(self):
        assert self.maxDepth != -1
        return self.maxDepth

n = input()
xml = ''
for i in range(n):
    xml += raw_input()

target = MaxDepth()
parser = XMLParser(target=target)
parser.feed(xml)
maxDepth = parser.close()
print maxDepth-1
