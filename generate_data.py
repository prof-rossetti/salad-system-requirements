# generate_data.py

import code # to debug: `code.interact(local=locals())`
import os
from pprint import pprint
import random
import csv
from faker import Faker

fake = Faker()

#
# DEFINE REAL DATA
#

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

salads = [
    {
        "name":"APPLES, PEARS + CHEDDAR",
        "calories": 455,
        "description": "organic mesclun, shredded kale, apples, pears, basil, raw pecans, organic white cheddar, balsamic vinaigrette",
        "contains_gluten":False,
        "vegan_safe":False,
        "type":"seasonal"
    },
    {
        "name":"ROASTED TURKEY + BRUSSELS SPROUTS",
        "calories": 445,
        "description": "organic mesclun, chopped romaine, roasted brussels sprouts, roasted sweet potatoes, roasted turkey, cranberry vinaigrette",
        "contains_gluten":False,
        "vegan_safe":False,
        "type":"seasonal"
    },
    {
        "name":"CURRY CAULIFLOWER + QUINOA",
        "calories": 550,
        "description": "organic quinoa + farro, organic arugula, roasted curry cauliflower, cilantro, raisins, roasted chicken, sriracha, cucumber tahini yogurt",
        "contains_gluten":True,
        "vegan_safe":False,
        "type":"seasonal"
    },
   {
        "name":"RAD THAI",
        "calories": 375,
        "description": "organic arugula + organic mesclun, sprouts, carrots, shredded cabbage, spicy sunflower seeds, cucumbers, basil, citrus shrimp, spicy cashew dressing",
        "contains_gluten":False,
        "vegan_safe":False,
        "type":"signature"
    },
   {
        "name":"KALE CAESAR",
        "calories": 430,
        "description": "shredded kale + chopped romaine, tomatoes, shaved parmesan, parmesan crisp, roasted chicken, fresh lime squeeze, caesar dressing",
        "contains_gluten":False,
        "vegan_safe":False,
        "type":"signature"
    },
   {
        "name":"SPICY SABZI",
        "calories": 430,
        "description": "organic baby spinach + shredded kale, spicy quinoa, spicy broccoli, raw beets, carrots, sprouts, basil, roasted organic tofu, sriracha, carrot chili vinaigrette",
        "contains_gluten":False,
        "vegan_safe":False,
        "type":"signature"
    },
   {
        "name":"GUACAMOLE GREENS",
        "calories": 540,
        "description": "organic mesclun, tomatoes, red onion, tortilla chips, avocado, roasted chicken, fresh lime squeeze, lime cilantro jalapeno vinaigrette",
        "contains_gluten":False,
        "vegan_safe":False,
        "type":"signature"
    },
   {
        "name":"AVOCOBBO",
        "calories": 705,
        "description": "shredded kale + chopped romaine, tomatoes, raw corn, avocado, bacon, egg, roasted chicken, blue cheese dressing",
        "contains_gluten":False,
        "vegan_safe":False,
        "type":"signature"
    },
   {
        "name":"HUMMUS TAHINA",
        "calories": 610,
        "description": "shredded kale + chopped romaine, tomatoes, red onion, cucumbers, pita chips, local feta, housemade hummus, baked falafel, cucumber tahini yogurt",
        "contains_gluten":True,
        "vegan_safe":False,
        "type":"signature"
    },
    {
        "name":"CUSTOM",
        "description": "make your own",
        "contains_gluten":None,
        "vegan_safe":None,
        "type":"custom"
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

#
# BASES
# ... Choose up to 2. All bases are gluten-free except quinoa + farro.

salad_bases = [
    "chopped romaine",
    "organic mesclun",
    "organic wild rice",
    "organic baby spinach",
    "shredded kale",
    "organic arugula",
    "organic quinoa + farro"
]

#
# INGREDIENTS
# ... Choose up to 4. Our vegetables are sourced locally when in season. Check your in-store local list for the most up-to-date lineup of farms and seasonal ingredients.

ingredients = [
    "roasted brussels sprouts",
    "roasted sweet potatoes",
    "pears",
    "apples",
    "raisins",
    "raw pecans",
    "basil",
    "cilantro",
    "local apples",
    "organic chickpeas",
    "spicy broccoli",
    "organic carrots",
    "sprouts",
    "raw corn",
    "shredded cabbage",
    "tomatoes",
    "raw beets",
    "spicy quinoa",
    "cucumbers",
    "red and green peppers",
    "red onion",
    "roasted sweet potatoes",
    "toasted almonds",
    "raw seeds",
    "spicy sunflower seeds",
    "pita chips", # contains gluten
    "tortilla chips"
]

#
# PREMIUMS
# ... Premiums include everything from local cheeses to vegan-friendly proteins.

premiums = [
    "roasted turkey",
    "roasted curry cauliflower",
    "local goat cheese",
    "local feta",
    "organic white cheddar",
    "shaved parmesan",
    "parmesan crisp",
    "avocado",
    "roasted chicken",
    "citrus shrimp",
    "hard boiled egg",
    "bacon",
    "roasted organic tofu",
    "baked falafel", # contains gluten
    "housemade hummus"
]

#
# DRESSINGS
# ... All of our dressings are gluten-free and made in-house.

dressings = [
    "cranberry vinaigrette",
    "spicy cashew dressing",
    "blue cheese dressing",
    "pesto vinaigrette",
    "balsamic vinaigrette",
    "caesar dressing",
    "cucumber tahini yogurt",
    "lime cilantro jalapeno vinaigrette",
    "miso sesame ginger vinaigrette",
    "carrot chili vinaigrette",
    "balsamic vinegar",
    "extra virgin olive oil",
    "fresh lime squeeze",
    "fresh lemon squeeze",
    "sriracha"
]





















payment_methods = ["cash","credit-card","mobile-app"]










#
# CREATE CSV FILE WITH HEADERS
#

orders_dot_csv = os.path.join(os.path.dirname(__file__), "data/orders.csv")
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": orders_dot_csv}
os.remove(orders_dot_csv) if os.path.isfile(orders_dot_csv) else "NO CSV FILE DETECTED"
orders_csv = csv.writer(open(orders_dot_csv, "w"), lineterminator=os.linesep)
orders_csv.writerow([
  "menu_item_name",
  "menu_item_price",
  "payment_authorized_at",
  "payment_id",
  "payment_method",
  "cc_name",
  "cc_number",
  "cc_exp",
  "payment_amount"
])

#
# GENERATE FAKE DATA
#

#rand_item = random.choice(items)
#print rand_item
#
#rand_items = random.sample(items, 3)
#print rand_items

#code.interact(local=locals())

#def name_of(obj):
#    return obj["name"]
#salad_names = map(name_of, salads)
#salad_names.append("CUSTOM")

payment_auth_times = []
for _ in range(1,114):
    dt = fake.date_time_this_year(before_now=True, after_now=False)
    payment_auth_times.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
payment_auth_times.sort()

menu_items = salads + seasonal_items + signature_grains

payment_id = 1
for payment_auth_time in payment_auth_times:
    payment_method = random.choice(payment_methods)
    credit_card_name = "todo"
    credit_card_number = "todo"
    credit_card_expiration = "todo"
    payment_amount = "todo"

    item_count = 3
    for _ in range(1,item_count):
        menu_item = random.choice(menu_items) # todo: skew toward salads?
        menu_item_price = "todo"

        row = {
            "menu_item_name": menu_item["name"],
            "menu_item_price": menu_item_price,
            "payment_authorized_at": payment_auth_time,
            "payment_id": payment_id,
            "payment_method": payment_method,
            "cc_name": credit_card_name,
            "cc_number": credit_card_number,
            "cc_exp": credit_card_expiration,
            "payment_amount": payment_amount
        }
        #orders_csv.writerow(row.values())
        orders_csv.writerow([
            row["menu_item_name"],
            row["menu_item_price"],
            row["payment_authorized_at"],
            row["payment_id"],
            row["payment_method"],
            row["cc_name"],
            row["cc_number"],
            row["cc_exp"],
            row["payment_amount"]
        ])

    payment_id+=1
