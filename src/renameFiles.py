import os
import re

def rename(material,number):
    os.chdir('/../dataset/{}'.format(material))
    n = number
    for f in os.listdir():
        new_name = re.sub("\d+", str(material) + str(n), f)
        #print(re.sub("R_\d+", "plastic"+str(n), f))
        n += 1
        os.rename(f, new_name)