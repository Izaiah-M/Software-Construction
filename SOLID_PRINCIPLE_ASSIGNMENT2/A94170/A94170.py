from abc import ABC, abstractmethod

# Interface for ReportGenerator
class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, employee):
        pass

# Interface for BonusCalculator
class BonusCalculator(ABC):
    @abstractmethod
    def calculate_bonus(self, employee):
        pass

# Abstract Employee class
class Employee(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def calculate_bonus(self):
        pass

# Manager class implementing Employee
class Manager(Employee):
    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

# Developer class implementing Employee
class Developer(Employee):
    def calculate_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

# Report class implementing ReportGenerator
class Report(ReportGenerator):
    def generate_report(self, employee):
        print(f"{employee.role} Report: {employee.name}")

# BonusCalculator class implementing BonusCalculator
class BonusCalculatorImpl(BonusCalculator):
    def calculate_bonus(self, employee):
        return employee.calculate_bonus()

if __name__ == "__main__":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    report_generator = Report()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    bonus_calculator = BonusCalculatorImpl()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    manager.manage_team()
    developer.code_review()

# Each class now has a single responsibility.
# The code is open for extension but closed for modification, as new functionality can be added without altering existing code.
# The Employee class acts as an abstraction, and both Manager and Developer inherit from it.
# ReportGenerator and BonusCalculator are abstract classes defining interfaces.
# Dependency inversion is achieved as high-level modules depend on abstractions (ReportGenerator, BonusCalculator) rather than concrete implementations.