import os
ENV1 = os.getenv('ENV1')
ENV2 = os.getenv('ENV2')
 
#script with arg

import sys
print ("The script has the name %s" % (sys.argv[0]))
arguments = len(sys.argv) - 1
print ("The script is called with %i arguments" % (arguments))

import time
print ("Update 1 of 5...");
time.sleep(5)
print ("Update 2 of 5...");
time.sleep(5)
print ("Update 3 of 5...");
time.sleep(5)
print ("Update 4 of 5...");
time.sleep(5)
print ("Update 5 of 5...");

print ("Done, thanks for waiting!");