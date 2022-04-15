
class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):

        if quota >= sum(self.sales):
            return True
        else:
            return False

    def compare_to(self, other):

        other_sales = other.total_sales()
        sales = self.total_sales()

        if other_sales > sales:
            return -1

        elif sales > other_sales:
            return 1

        else:
            return 0

    def __str__(self):
        id = self.get_id()
        name = self.get_name()
        total_sales = self.total_sales()
        return '{}-{}-{}'.format(id, name, total_sales)
