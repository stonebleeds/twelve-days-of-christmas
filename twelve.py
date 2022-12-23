#!/usr/bin/python2
#prints out entire lyrics to The 12 Days Of Christmas
#v0.3
import sys
a = { 1: "a partridge in a pear tree.",
    2: "two turtle doves, and",
    3: "three french hens,",
    4: "four calling birds,",
    5: "five golden rings,",
    6: "six geese a laying,",
    7: "seven swans a swimming,",
    8: "eight maids a milking,",
    9: "nine ladies dancing,",
    10: "ten lords a leaping,",
    11: "eleven pipers piping,",
    12: "twelve drummers drumming,"
}

b = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
for j in range(1,13):
    print "On the",b[j-1],"day of Christmas, my true love gave to me ",
    for i in range(j,0,-1): sys.stdout.write(a[i]+' ')
    sys.stdout.write("\r\n")
    sys.stdout.flush()
