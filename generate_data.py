# generate_data.py

#import code # to debug: `code.interact(local=locals())`
#import os
#from pprint import pprint
#from random import choice, sample
import random
#import json
#import csv

items = ["zero",1,2,3,4,"five",6,7,"eight",9]

for item in items:
    print item

rand_item = random.choice(items)
print rand_item

rand_items = random.sample(items, 3)
print rand_items
