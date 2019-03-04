def change(arg):
    print "    ch   - id ", id(arg), "value: ", arg
    arg = 0
    print "    ch   - id ", id(arg), "value: ", arg


def changeList(arg):
    print "    ch L1- id ", id(arg), "value: ", arg
    arg[0] = 0
    print "    ch L1- id ", id(arg), "value: ", arg


def changeList2(arg):
    print "    ch L2- id ", id(arg), "value: ", arg
    arg = [0]
    print "    ch L2- id ", id(arg), "value: ", arg


value = 99
print "main     - id ", id(value), "value: ", value
change(value)
print "main     - id ", id(value), "value: ", value
print ""

value = [99]
print "main     - id ", id(value), "value: ", value
changeList2(value)
print "main     - id ", id(value), "value: ", value
print ""

value = [99]
print "main     - id ", id(value), "value: ", value
changeList(value)
print "main     - id ", id(value), "value: ", value
