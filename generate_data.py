# generate_data.py

import code # to debug: `code.interact(local=locals())`
#import os
from pprint import pprint
#from random import choice, sample
import random
#import json
#import csv

#rand_item = random.choice(items)
#print rand_item
#
#rand_items = random.sample(items, 3)
#print rand_items

'''
    {
        "name":"_______",
        "calories": 0000000,
        "description": "_________",
        "contains_gluten":False,
        "vegan_safe":False
    },
'''

seasonal_items = [
    {
        "name":"CRANBERRY PEAR FRESCA",
        "calories": 60,
        "description": "a refreshing, lightly sweet beverage made of just pears, cranberries, ginger, lemons and water",
        "contains_gluten":False,
        "vegan_safe":True
    },
    {
        "name":"ORGANIC BUTTERNUT SQUASH",
        "calories": "120-180",
        "description": "a smooth and rich soup to warm you up in cold weather",
        "contains_gluten":False,
        "vegan_safe":False
    },
    {
        "name":"ORGANIC LENTIL CHICKPEA SOUP",
        "calories": "160-240",
        "description": "this 100% organic soup is made with hearty lentils and chickpeas with diced carrots, onions and celery",
        "contains_gluten":False,
        "vegan_safe":True
    }
]

seasonal_salads = [
    {
        "name":"APPLES, PEARS + CHEDDAR",
        "calories": 455,
        "description": "organic mesclun, shredded kale, apples, pears, basil, raw pecans, organic white cheddar, balsamic vinaigrette",
        "contains_gluten":False,
        "vegan_safe":False
    },
    {
        "name":"ROASTED TURKEY + BRUSSELS SPROUTS",
        "calories": 445,
        "description": "organic mesclun, chopped romaine, roasted brussels sprouts, roasted sweet potatoes, roasted turkey, cranberry vinaigrette",
        "contains_gluten":False,
        "vegan_safe":False
    },
    {
        "name":"CURRY CAULIFLOWER + QUINOA",
        "calories": 550,
        "description": "organic quinoa + farro, organic arugula, roasted curry cauliflower, cilantro, raisins, roasted chicken, sriracha, cucumber tahini yogurt",
        "contains_gluten":True,
        "vegan_safe":False
    }
]

signature_salads = [
   {
        "name":"RAD THAI",
        "calories": 375,
        "description": "organic arugula + organic mesclun, sprouts, carrots, shredded cabbage, spicy sunflower seeds, cucumbers, basil, citrus shrimp, spicy cashew dressing",
        "contains_gluten":False,
        "vegan_safe":False
    },
   {
        "name":"KALE CAESAR",
        "calories": 430,
        "description": "shredded kale + chopped romaine, tomatoes, shaved parmesan, parmesan crisp, roasted chicken, fresh lime squeeze, caesar dressing",
        "contains_gluten":False,
        "vegan_safe":False
    },
   {
        "name":"SPICY SABZI",
        "calories": 430,
        "description": "organic baby spinach + shredded kale, spicy quinoa, spicy broccoli, raw beets, carrots, sprouts, basil, roasted organic tofu, sriracha, carrot chili vinaigrette",
        "contains_gluten":False,
        "vegan_safe":False
    },
   {
        "name":"GUACAMOLE GREENS",
        "calories": 540,
        "description": "organic mesclun, tomatoes, red onion, tortilla chips, avocado, roasted chicken, fresh lime squeeze, lime cilantro jalapeno vinaigrette",
        "contains_gluten":False,
        "vegan_safe":False
    },
   {
        "name":"AVOCOBBO",
        "calories": 705,
        "description": "shredded kale + chopped romaine, tomatoes, raw corn, avocado, bacon, egg, roasted chicken, blue cheese dressing",
        "contains_gluten":False,
        "vegan_safe":False
    },
   {
        "name":"HUMMUS TAHINA",
        "calories": 610,
        "description": "shredded kale + chopped romaine, tomatoes, red onion, cucumbers, pita chips, local feta, housemade hummus, baked falafel, cucumber tahini yogurt",
        "contains_gluten":True,
        "vegan_safe":False
    }
]

signature_grains = [
    {
         "name":"EARTH BOWL",
         "calories": 775,
         "description": "quinoa + farro, organic arugula, tomatoes, raw corn, organic chickpeas, spicy broccoli, organic white cheddar, roasted chicken, pesto vinaigrette",
         "contains_gluten":True,
         "vegan_safe":False
     },
    {
         "name":"HARVEST BOWL",
         "calories": 685,
         "description": "organic wild rice + shredded kale, apples, sweet potatoes, toasted almonds, local goat cheese, roasted chicken, balsamic vinaigrette",
         "contains_gluten":False,
         "vegan_safe":False
     },
    {
         "name":"WILD CHILD",
         "calories": 545,
         "description": "organic wild rice + organic baby spinach, cilantro, peppers, raw beets, shredded cabbage, carrots, raw seeds, avocado, miso sesame ginger dressing",
         "contains_gluten":True,
         "vegan_safe":False
     }
]

salads = seasonal_salads + seasonal_items + signature_salads + signature_grains

for salad in salads:
    pprint(salad)
    #code.interact(local=locals())
