class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Interface for report generation
class ReportGenerator:
    def generate_report(self, employee):
        raise NotImplementedError("Subclasses must implement generate_report method")

# Concrete class for manager report generation
class ManagerReportGenerator(ReportGenerator):
    def generate_report(self, manager):
        print(f"Manager Report: {manager.name}")

# Concrete class for developer report generation
class DeveloperReportGenerator(ReportGenerator):
    def generate_report(self, developer):
        print(f"Developer Report: {developer.name}")

# Interface for bonus calculation
class BonusCalculator:
    def calculate_bonus(self, employee):
        raise NotImplementedError("Subclasses must implement calculate_bonus method")
    
# Concrete class for manager bonus calculation
class ManagerBonusCalculator(BonusCalculator):
    def calculate_bonus(self, manager):
        return manager.calculate_manager_bonus()   

# Concrete class for developer bonus calculation
class DeveloperBonusCalculator(BonusCalculator):
    def calculate_bonus(self, developer):
        return developer.calculate_developer_bonus()
    
class Manager(Employee):
    def calculate_manager_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def calculate_developer_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

if __name__ == "__main__":
    # Example usage
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    # Creating instances for report generation
    manager_report_generator = ManagerReportGenerator()
    developer_report_generator = DeveloperReportGenerator()

    # Generating reports
    manager_report_generator.generate_report(manager)
    developer_report_generator.generate_report(developer)