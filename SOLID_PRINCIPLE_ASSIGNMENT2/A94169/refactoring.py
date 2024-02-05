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

