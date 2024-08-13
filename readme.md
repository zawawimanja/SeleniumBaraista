1. Private Methods

Private methods are functions defined within a class but cannot be accessed directly from outside the class. They are typically used for helper functions or internal logic that doesn't need external access.

2. Inheritance

Inheritance allows creating new classes (subclasses) that inherit properties and behaviors from existing classes (parent classes). This promotes code reusability and reduces redundancy.

3. Composition

Composition involves creating objects of one class and using them within another class. This allows for building complex functionalities by combining simpler components.

4. Abstraction & Interface

Abstraction focuses on hiding implementation details and exposing essential functionalities to users. Interfaces define contracts with methods, forcing subclasses to implement the required behavior.

5. Configuration Management

Configuration management refers to storing and organizing test automation settings (URLs, credentials, etc.) in separate files for easier maintenance and flexibility.

6. Error Handling & Logging

Robust test automation involves handling potential errors gracefully and logging them for analysis. This helps identify and address issues during test execution.

7. Data Driven Testing

Data driven testing involves separating test cases from test data. Different data sets can be used with the same test logic, allowing for efficient testing of various scenarios.

8. Chaining Methods

Chaining methods refers to calling multiple methods sequentially on the same object. This improves code readability and maintainability for complex interactions.

9. POM (Page Object Model) + Factory Pattern

The POM pattern separates page objects (elements, actions) from test logic. The Factory pattern simplifies page object creation and reduces code duplication.

10. BDD (Behavior Driven Development) - Cucumber

BDD promotes test creation based on user behavior. Cucumber is a popular BDD framework that allows writing test scenarios in a human-readable format (gherkin syntax).

11. Encapsulation

    ---------------------------------------------------------------------------------------------------------------------------------

a. ID is typically the most unique and stable locator.
b. XPath and CSS Selectors are highly customizable and can be made unique, but they can be fragile if the DOM structure changes.
c. Name is somewhat unique but less reliable than ID.
d. Class Name is less unique and may be shared by multiple elements.
