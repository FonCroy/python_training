# -*- coding: utf-8 -*-
import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.group import Group


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
output_file = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        output_file = a

def random_string(prefix, max_len):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(max_len))])


test_data = [Group("", "", "")] + \
            [Group(random_string("name", 10), random_string("header", 20), random_string("footer", 20))
             for i in range(n)
             ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_file)
with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(test_data))
