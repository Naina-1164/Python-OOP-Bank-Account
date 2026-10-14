"""SalesReport V2: practice reusable methods with a list of sales."""

class SalesReport:
    def __init__(self, sales):
        self.sales = sales

    def total_sales(self):
        return sum(self.sales)

    def average_sales(self):
        return self.total_sales() / len(self.sales)

    def highest_sales(self):
        return max(self.sales)

    def lowest_sales(self):
        return min(self.sales)

    def sales_difference(self):
        return self.highest_sales() - self.lowest_sales()


weekly_sales = [1200, 1500, 1100, 1800, 2100, 2500, 1700]
report = SalesReport(weekly_sales)
print("WEEKLY SALES REPORT")
print("-------------------")
print("Total Sales:", report.total_sales())
print("Average Sales:", report.average_sales())
print("Highest Sales:", report.highest_sales())
print("Lowest Sales:", report.lowest_sales())
print("Sales Difference:", report.sales_difference())
