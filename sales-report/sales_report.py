"""Beginner Python OOP project: weekly sales report."""


class SalesReport:
    """Store weekly sales data and calculate simple sales statistics."""

    def __init__(self, sales_data):
        self.sales_data = sales_data

    def total_sales(self):
        """Return total sales for the week."""
        return sum(self.sales_data.values())

    def average_sales(self):
        """Return average daily sales."""
        return self.total_sales() / len(self.sales_data)

    def best_day(self):
        """Return the day and sales amount with the highest sales."""
        day = max(self.sales_data, key=self.sales_data.get)
        return day, self.sales_data[day]

    def above_average_days(self):
        """Return all days with sales above the weekly average."""
        average = self.average_sales()
        return [
            day
            for day, amount in self.sales_data.items()
            if amount > average
        ]


sales = {
    "Monday": 1200,
    "Tuesday": 1500,
    "Wednesday": 1100,
    "Thursday": 1800,
    "Friday": 2100,
    "Saturday": 2500,
    "Sunday": 1700,
}

report = SalesReport(sales)

best_day, best_sales = report.best_day()
above_average = ", ".join(report.above_average_days())

print("Weekly Sales Report")
print("-------------------")
print(f"Total Sales: {report.total_sales()}")
print(f"Average Sales: {report.average_sales():.0f}")
print(f"Best Day: {best_day} ({best_sales})")
print(f"Above Average Days: {above_average}")
