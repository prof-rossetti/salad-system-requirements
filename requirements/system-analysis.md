# System Analysis

## System Justification

Although the "Salad System" implementation will cost thousands of dollars
 in upfront and ongoing software and hardware costs,
 it will save the company money in the long run
  by avoiding hundreds of thousands of dollars in unnecessary legal fees
  and thousands of dollars in payroll costs.

## System Objectives

 1. Display a digital menu with accuracy
 2. Automate the menu update process
 3. Process payments
 4. Capture and store a comprehensive history of orders and payments
 5. Support executives in decision-making

## Information Requirements

For each order,
 executives are only interested in knowing
  which menu item was ordered and the
  total price of the order
   as affected by price overages
    as applicable.
 Executives track ingredient supply and consumption levels using a separate system.

### Information Inputs

1. Menu Metadata
2. Order Details
2. Customer Payment Information

The company currently describes each menu item and ingredient,
 and categorizes each in terms of its calorie count, gluten composition, and vegan-friendliness. The system needs this menu item metadata to properly display the menu.

To store a comprehensive transaction history,
 the system needs to capture data about each order and payment.

To process customer payments, in some cases the system requires customer credit card information.

### Information Outputs

1. Digital Menu
2. Order and Payment Transaction History Report
3. Order Summary Charts

The system should display a clear and accurate digital representation of menu information.

The system should produce a .csv report of comprehensive order and payment information to facilitate manual and programmatic data analysis.

The system should summarize order and payment data in visual form to aid decision-making.
