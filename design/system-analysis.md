# Salad Information System Analysis

## Business Problem

The Urban Lunch Company has an opportunity
 to introduce efficiency and effectiveness into the menu creation and update processes
  by transitioning from
   a hand-written menu board
   to a wall-mounted digital display.

The company creates a new core menu each season, and updates the menu on a regular basis to reflect changes in food sourcing and pricing.

When a menu is created or updated, an employee  manually removes the large chalkboard from the wall, translates the information onto the chalkboard, and hangs it back up on the wall. Sometimes the employee stands on a stool or ladder to obviate need to lift the chalkboard.

This manual process costs employee time and therefore company resources.

Past manual errors in denoting menu item gluten content have led to customer allergy attacks and pending lawsuits.

## System Solution

### System Justification

Although the "Salad System" implementation will cost thousands of dollars in upfront and ongoing software and hardware costs, it will save the company money in the long run by avoiding hundreds of thousands of dollars in unnecessary legal fees and thousands of dollars in payroll costs.

### System Objectives

 1. Display digital menu with accuracy
 2. Automate the menu update process
 3. Capture and store a comprehensive history of orders and payments
 4. Process payments
 6. Support executives in making data-driven management decisions

The system should perform current processes like payment processing, as well as new processes like automated menu updating. As an added bonus, the new system should also provide supply-chain and staffing decision-making support to company executives.

### Information Requirements

#### Information Inputs

1. Menu Item Metadata
2. Order Details
2. Customer Payment Information

The company currently describes each menu item and ingredient,
 and categorizes each in terms of its calorie count, gluten composition, and vegan-friendliness. The system needs this menu item metadata to properly display the menu.

To store a comprehensive transaction history, the system needs data about each order.

In order to process customer payments, in some cases the system requires customer credit card information.

#### Information Outputs

1. Digital Menu
2. Order and Payment Transaction History Report
3. Order Summary Charts

The system should display a clear and accurate digital representation of menu information.

The system should produce a .csv report of comprehensive order and payment information to facilitate manual and programmatic data analysis. **For each order, executives are only interested in knowing which menu item was ordered and the total price of the order as affected by price overages as applicable; executives choose to track ingredient supply and consumption levels using a separate system.**

The system should summarize order and payment data in visual form to aid decision-making.
