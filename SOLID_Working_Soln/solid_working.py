from abc import ABC, abstractmethod

# This is the base class representing an employee with a name and role
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Interface defining the contract for writing a report
class ReportWriter(ABC):
    @abstractmethod
    def write_report(self, employee):
        pass

# Interface defining the contract for calculating bonuses
class BonusCalculator(ABC):
    @abstractmethod
    def calculate_bonus(self, employee):
        pass

# This is the implementation for writing a report for a Manager
class ManagerReportWriter(ReportWriter):
    def write_report(self, manager):
        print(f"Manager Report: {manager.name}")

# This is the implementation for writing a report for a Developer
class DeveloperReportWriter(ReportWriter):
    def write_report(self, developer):
        print(f"Developer Report: {developer.name}")

# This is the implementation for calculating bonuses for a Manager
class ManagerBonusCalculator(BonusCalculator):
    def calculate_bonus(self, manager):
        return 1000

# This is the implementation for calculating bonuses for a Developer
class DeveloperBonusCalculator(BonusCalculator):
    def calculate_bonus(self, developer):
        return 500

# Interface defining the contract for managerial roles
class ManagerRole(ABC):
    @abstractmethod
    def manage_team(self):
        pass

# Interface defining the contract for developer roles
class DeveloperRole(ABC):
    @abstractmethod
    def code_review(self):
        pass

# This is the implementation of a Manager with specific role-related actions
class Manager(Employee, ManagerRole):
    def manage_team(self):
        print(f"{self.name} is managing the team.")

# This is the implementation of a Developer with specific role-related actions
class Developer(Employee, DeveloperRole):
    def code_review(self):
        print(f"{self.name} is conducting a code review.")

if __name__ == "__main__":
    # Creating instances of Manager and Developer
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    # Creating instances of report writers and bonus calculators for each role
    manager_report_writer = ManagerReportWriter()
    developer_report_writer = DeveloperReportWriter()
    manager_bonus_calculator = ManagerBonusCalculator()
    developer_bonus_calculator = DeveloperBonusCalculator()

    # Generating reports for Manager and Developer
    manager_report_writer.write_report(manager)
    developer_report_writer.write_report(developer)

    # Calculating bonuses for Manager and Developer
    manager_bonus = manager_bonus_calculator.calculate_bonus(manager)
    developer_bonus = developer_bonus_calculator.calculate_bonus(developer)

    # Displaying the calculated bonuses
    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    # Performing role-specific actions
    manager.manage_team()
    developer.code_review()


# Changes Made:
# Introduced interfaces for report writing and bonus calculation.
# Implemented concrete classes for each role's report writing and bonus calculation.
# Used dependency injection to decouple report generation and bonus calculation from specific implementations.
# Ensured that each role adheres to its specific interface, promoting adherence to LSP.
# Reorganized the code to adhere to SRP, OCP, ISP, and DIP principles.