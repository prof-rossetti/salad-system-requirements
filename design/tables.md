# Physical Design

Legend:

PK = Primary Key
FK = Foreign Key
CFK = Composite Foreign Key (indicates polymorphism)
INDX = Regular Index
VA = Virtual Attribute (calculated, not stored)

## Tables

#### `regions`

 + `id` (PK)
 + `name`
 + `manager_id` (FK referencing `employees` table)

#### `locations`

 + `id` (PK)
 + `region_id` (FK referencing `regions` table)
 + `name`
 + `street_address`
 + `city`
 + `state`
 + `zip_code`
 + `latitude`
 + `longitude`
 + `weekday_lunch_service_starts_at` (assumes lunch service only during weekdays and same hours each day)
 + `weekday_lunch_service_ends_at` (assumes lunch service only during weekdays and same hours each day)

#### `employees`

 + `id` (PK)
 + `first_name`
 + `last_name`
 + `ssn`

#### `shifts` (out of scope)

#### `menus`

 + `id` (PK)
 + `region_id` (FK referencing `regions` table)
 + `effective_start`
 + `effective_end`

#### `menus_items` (or `menu_item_roles`)

 + `menu_id` (FK referencing `menus` table)
 + `item_id` (FK referencing `items` table)
 + `item_role`
 + `item_default_price`

#### `menus_ingredients` (or `menu_ingredient_roles`)

  + `menu_id`
  + `ingedient_id`
  + `ingedient_role`
  + `ingedient_overage_price`

#### `items`

 + `id`
 + `name`
 + `description`
 + `calories` (string, assumes for display purposes and not for calculation purposes)
 + `gluten_free` (VA calculated to be false if any component ingredient is false)
 + `vegan_safe` (VA false if any component ingredient is false)

#### `item_default_ingredients`

 + `item_id`
 + `ingredient_id`

#### `ingredients`

 + `id`
 + `name`
 + `description`
 + `gluten_free`
 + `vegan_safe`

#### `orders`

 + `id`
 + `type` ("Online" or "In-store")
 + `received_at`
 + `preparation_location_id` (FK referencing `locations` table)
 + `preparer_id` (FK referencing `employees` table)
 + `payment_amount_usd`
 + `payment_attendant_id` (FK referencing `employees` table)
 + `payment_method_type` (one half of a CFK referencing the Payment Method: "Credit Card","Cash","Mobile App","Gift Card", or "Legacy Loyalty Card")
 + `payment_method_id` (one half of a CFK referencing the Payment Method instance; applies only to "Credit Card" and "Gift Card" and "Mobile App" payment methods)
 + `payment_authorization_requested_at`
 + `payment_authorized_at`

todo: order for pickup or delivery? (delivery instructions)

#### `ordered_items`

 + `order_id`
 + `menu_item_id`
 + `preparation_instructions` (optional)
 + `price_overages` (optional, if)
 + `total_cost` (VA calculated from the normal menu item price plus any price overages)

#### `credit_cards`

 + `credit_card_number`
 + `cvv`
 + `expiration_year`
 + `expiration_month`
 + `zip_code` (billing)
 + `cardholder_name`

#### `customer_profiles`

 + `id`
 + `first_name`
 + `last_name`
 + `email_address`
 + `birth_date`
 + `gender`
 + `zip_code` (residential)
 + `password`
 + `qr_code`

#### `customer_dietary_preferences`

  + `customer_profile_id`
  + `vegetarian`
  + `vegan`
  + `gluten_free`
  + `nut_free`

#### `customer_credit_cards`

 + `customer_id`
 + `credit_card_number`
