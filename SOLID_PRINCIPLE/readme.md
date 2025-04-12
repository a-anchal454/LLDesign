## SOLID Principles in Object-Oriented Design

1. **S** – Single Responsibility Principle  
2. **O** – Open/Closed Principle  
3. **L** – Liskov Substitution Principle  
4. **I** – Interface Segregation Principle  
5. **D** – Dependency Inversion Principle

### 1. Single Responsibility Principle (SRP) 
A class should have only one reason to change.
This means that a class, module, or function should have only one job or responsibility. If it has more than one, those responsibilities become coupled, and changes to one may affect the others.

**Scenario:** Blog Application with SRP Applied

**Requirements:**

- Create a blog post
- Validate post data (title, content)
- Save the post to the database
- Send a notification email to subscribers

**Without SRP (Bad Practice)**
Everything is handled in a single class, violating SRP.
//code 


By following SRP, we'll create separate classes for each responsibility.
**1. Validation Service (Handles data validation)** 
// code 

**2. Post Service (Handles business logic)**
//code 

**3. Email Service (Handles email logic)**
//code 