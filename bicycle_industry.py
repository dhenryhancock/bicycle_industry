class bicycle(object):
    def __init__(self, model, production_cost, weight):
        self.model=model
        self.production_cost=production_cost
        self.weight=weight

bicycles=[bicycle("schwinn", 100, 20), bicycle("speedster", 120, 15)]

class bike_shop(object):
    def __init__(self, store_name, inventory, markup, profit):
        self.store_name=store_name
        self.inventory=inventory
        self.markup=markup
        self.profit=profit
    def purchase_inventory(self):
        self.inventory={}
        self.inventory_prices={}
        for bike in bicycles:
            bike_model=bike.model
            inventory_number=50
            bike_price=bike.production_cost * self.markup
            self.inventory[bike_model]=inventory_number
            self.inventory_prices[bike_model]=bike_price
    def sell_bike (self):
        self.inventory[model]-=1
        self.profit+=production_cost*self.markup

class customers(object):
    def __init__(self, customer_name, budget, bikes_owned):
        self.customer_name=customer_name
        self.budget=budget
        self.bikes_owned=bikes_owned
    def enter_store(self):
        shoppers.append(self.customer_name)
    def buy_bike(self, model, retail_price):
        customers.bikes_owned.append(model)
        customers.budget-=int(retail_price)

shoppers=[customers("Sally", 200, []), customers("Jim", 500, []), customers("Jane", 1000, [])]

bike_shops=[bike_shop("toms_store", {} , 1.20, 0 )]

toms_store.purchase_inventory()
