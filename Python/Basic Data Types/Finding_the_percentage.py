# Enter your code here. Read input from STDIN. Print output to STDOUT
entries = int(raw_input())
listEntry = {}
for i in xrange(entries):
    record = raw_input()
    record = record.split()
    listEntry[record[0]] = record[1:]
lastPerson = raw_input()
if lastPerson in listEntry:
    #map converts all elements in list to another type
    avge = sum(map(float,listEntry[lastPerson])) / float(len(listEntry[lastPerson]))
    print "%.2f" % avge
