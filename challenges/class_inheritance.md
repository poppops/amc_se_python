# **Python Inheritance Challenge**

## **Objective**  
Create a simple program that models a system of animals, showcasing inheritance in Python.

---

## **Instructions**  

1. **Create a base class** called `Animal` with the following attributes and methods:
   - **Attributes**: `name` (string), `species` (string)
   - **Method**: `describe()` - prints a message in the format:  
     `"This is [name], and it is a [species]."`

2. **Create a subclass** called `Dog` that inherits from `Animal`:
   - **Additional Attribute**: `breed` (string)
   - **Method Override**: Update the `describe()` method to include the breed:  
     `"This is [name], a [breed] [species]."`

3. **Create another subclass** called `Cat` that inherits from `Animal`:
   - **Additional Attribute**: `favorite_toy` (string)
   - **Method Override**: Update the `describe()` method to include the favorite toy:  
     `"This is [name], a [species] that loves playing with [favorite_toy]."`

4. **Instantiate the following objects** and call their `describe()` method:
   - A generic animal: `name = "Unknown"`, `species = "Unknown"`
   - A dog: `name = "Buddy"`, `species = "dog"`, `breed = "Golden Retriever"`
   - A cat: `name = "Whiskers"`, `species = "cat"`, `favorite_toy = "yarn"`

---

## **Expected Output**  
```plaintext
This is Unknown, and it is a Unknown.
This is Buddy, a Golden Retriever dog.
This is Whiskers, a cat that loves playing with yarn.