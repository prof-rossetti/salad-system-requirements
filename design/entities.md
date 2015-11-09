# Salad System

## Conceptual Design

This document represents work product from initial database planning and design processes.

The most recent [Entity Relationship Diagram (ERD)](diagrams/) supersedes this planning document.

### Entities

 + Employee
 + Location
 + Region
 + Menu
 + Menu Item
 + Menu Item Role (join entity)
 + Menu Item Default Ingredient (join table)
 + Menu Ingredient
 + Menu Ingredient Role (join entity)
 + Customer
 + Order
 + Ordered Item (join entity)
 + Payment Method (super-type)
 + Customer Profile
 + Customer Dietary Preference
 + Customer Credit Card
 + Credit Card

An `employee` is a person who
  has entered into a contractual labor agreement with the company to
  exchange labor and other services for wages.

A `location` represents a physical street address where the company operates lunch service.

A `region` is a collection of geographically-related locations.

A `menu` communicates food and drink options available during lunch service.
