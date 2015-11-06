# generate_data.py

import code # to debug: code.interact(local=locals())
import os
from pprint import pprint
import random
import json
import csv
from operator import itemgetter
from collections import OrderedDict
from faker import Faker
fake = Faker()

# todo: refactor

#
# MENU INGREDIENTS
#

# todo

#
# MENU ITEMS
#

custom_items_path = os.path.join(os.path.dirname(__file__), "inputs/menu/items/custom_items.json")
custom_items = json.loads(open(custom_items_path).read())["menu_items"]
seasonal_items_path = os.path.join(os.path.dirname(__file__), "inputs/menu/items/seasonal_items.json")
seasonal_items = json.loads(open(seasonal_items_path).read())["menu_items"]
seasonal_salads_path = os.path.join(os.path.dirname(__file__), "inputs/menu/items/seasonal_salads.json")
seasonal_salads = json.loads(open(seasonal_salads_path).read())["menu_items"]
signature_grains_path = os.path.join(os.path.dirname(__file__), "inputs/menu/items/signature_grains.json")
signature_grains = json.loads(open(signature_grains_path).read())["menu_items"]
signature_salads_path = os.path.join(os.path.dirname(__file__), "inputs/menu/items/signature_salads.json")
signature_salads = json.loads(open(signature_salads_path).read())["menu_items"]
menu_items = custom_items + seasonal_items + seasonal_salads + signature_grains + signature_salads

menu_items_dot_csv = os.path.join(os.path.dirname(__file__), "data/menu_items.csv")
os.remove(menu_items_dot_csv) if os.path.isfile(menu_items_dot_csv) else "NO CSV FILE DETECTED"
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": menu_items_dot_csv}
menu_items_csv = csv.writer(open(menu_items_dot_csv, "w"), lineterminator=os.linesep)
menu_item_headers = menu_items[0].keys()
menu_item_headers.sort()
menu_items_csv.writerow(menu_item_headers)

for menu_item in menu_items:
    row = OrderedDict(sorted(menu_item.items()))
    menu_items_csv.writerow(row.values())
    print(row.values())

#
# CUSTOMERS
#

customers_dot_csv = os.path.join(os.path.dirname(__file__), "data/customers.csv")
os.remove(customers_dot_csv) if os.path.isfile(customers_dot_csv) else "NO CSV FILE DETECTED"
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": customers_dot_csv}
customers_csv = csv.writer(open(customers_dot_csv, "w"), lineterminator=os.linesep)
customer_headers = ["cc_name","cc_number","cc_exp","qr_code"]
customer_headers.sort()
customers_csv.writerow(customer_headers)

customers = []
for _ in range(1,77):
    customer = {
        "cc_name": "%(first)s %(last)s" % {"first": fake.first_name(), "last": fake.last_name() },
        "cc_number": fake.credit_card_number(card_type=None),
        "cc_exp": fake.credit_card_expire(start="now", end="+6y", date_format="%m/%y"),
        "qr_code": fake.ean(length=13)
    }
    customers.append(customer)
    row = OrderedDict(sorted(customer.items()))
    customers_csv.writerow(row.values())
    print(row.values())



#
# PAYMENTS
#

payment_methods = ["cash","credit-card","mobile-app"]
payments = []
payment_id = 1
for _ in range(1,27):
    payment_auth_at = fake.date_time_this_year(before_now=True, after_now=False)
    payment_method = random.choice(payment_methods) #todo: skew toward cards
    customer = random.choice(customers)
    payment = {
        "id": payment_id,
        "method": payment_method,
        "authorized_at": payment_auth_at.strftime('%Y-%m-%d %H:%M:%S'),
        "cc_name": customer["cc_name"] if payment_method in ["credit-card","mobile-app"] else None,
        "cc_number": customer["cc_number"] if payment_method in ["credit-card","mobile-app"] else None,
        "cc_exp": customer["cc_exp"] if payment_method in ["credit-card","mobile-app"] else None,
        "qr_code": customer["qr_code"] if payment_method == "mobile-app" else None
    }
    payments.append(payment)
payments = sorted(payments, key=itemgetter('authorized_at'))

#
# ORDER HISTORY REPORT
#

order_history_dot_csv = os.path.join(os.path.dirname(__file__), "outputs/reports/order_history.csv")
os.remove(order_history_dot_csv) if os.path.isfile(order_history_dot_csv) else "NO CSV FILE DETECTED"
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": order_history_dot_csv}
order_history_csv = csv.writer(open(order_history_dot_csv, "w"), lineterminator=os.linesep)
order_history_headers = [
  "menu_item_name","menu_item_price", # "price_overages"
  "payment_method","payment_amount",
  "payment_id","payment_authorized_at",
  "cc_name","cc_number","cc_exp","qr_code"
]
order_history_headers.sort()
order_history_csv.writerow(order_history_headers)
print(order_history_headers)

for payment in payments:
    item_count = random.choice([1,2,3]) # todo: skew towards 1
    for _ in range(1,item_count):
        menu_item = random.choice(menu_items) # todo: skew toward salads
        order = {
            "menu_item_name": menu_item["name"],
            "menu_item_price": 9.99, #todo: menu_item["price"]
            "payment_authorized_at": payment["authorized_at"],
            "payment_id": payment["id"],
            "payment_method": payment["method"],
            "cc_name": customer["cc_name"],
            "cc_number": customer["cc_number"],
            "cc_exp": customer["cc_exp"],
            "qr_code": customer["qr_code"],
            "payment_amount": 0.00 #todo: sum up price of all orders
        }
        row = OrderedDict(sorted(order.items()))
        order_history_csv.writerow(row.values())
        print(row.values())

    payment_id+=1




# BASES ... Choose up to 2. All bases are gluten-free except quinoa + farro.
# INGREDIENTS ... Choose up to 4. Our vegetables are sourced locally when in season. Check your in-store local list for the most up-to-date lineup of farms and seasonal ingredients.
# PREMIUMS ... Premiums include everything from local cheeses to vegan-friendly proteins.
# DRESSINGS ... All of our dressings are gluten-free and made in-house.




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
