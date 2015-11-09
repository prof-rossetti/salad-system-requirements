# Salad System

## Conceptual Design

This document represents work product from initial database planning and design processes.

The most recent [Entity Relationship Diagram (ERD)]([diagrams](diagrams/) supersedes this planning document.

### Entity Relationships

 + Employee / Region
 + Employee / Location
   + FoodPreparer / Location
   + Salesperson / Location
 + CustomerProfile /
 + Menu / Menu Item

#### Employee / Region

 An employee called the `regional_manager` manages zero or more regions.

 A `region` is managed by one employee, called the `regional_manager`.

#### Employee / Location

There are two direct relationships between the Employee and Location entities.

##### Food Preparer / Location

An employee called the `food_preparer` prepares food at zero or many `locations`, although not more than one at the same time.

A `location` has one or more employees working as `food_preparers` at any given time during lunch service, perhaps with more than one operating in the same location at the same time.



##### Salesperson / Location

An employee called the payment-station-attendant, or `salesperson`, attends one of the payment stations at zero or many `locations`, although not more than one at the same time.

A `location` has one or more `salespeople` operating a payment station at any time during lunch service, perhaps with more than one operating in the same location at the same time.
