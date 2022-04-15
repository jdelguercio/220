
class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        for line in file:
            self.sales_people.append(line)

    def quota_report(self, quota):
        out_list = []
        for sales_person in self.sales_people:
            list_var = []
            id, name, sales = ','.split(sales_person)
            sales = ' '.split(sales)
            sales = sum(sales)
            list_var.append(id)
            list_var.append(name)
            list_var.append(sales)

            if sales >= quota:
                quo = True
            else:
                quo = False

            list_var.append(quo)
            out_list.append(list_var)

    def top_seller(self):
        top_sales = 0
        top_bois = []
        for sales_person in self.sales_people:
            id, name, sales = ','.split(sales_person)
            sales = ' '.split(sales)
            sales = sum(sales)

            if sales >= top_sales:
                top_sales = sales
                top_bois.append(name)
            else:
                pass
