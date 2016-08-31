class bicycle(object):
    def __init__(self, model, production_cost, weight):
        self.model=model
        self.production_cost=production_cost
        self.weight=weight
        self.bicycles=bicycles
    def new_model(self):
        bicycles.append(self.model) 

class bike_shop(object):
    def __init__(self, store_name, inventory, markup, profit):
        self.store_name=store_name
        self.inventory=inventory
        self.markup=markup
        self.profit=profit
    def purchase_inventory (self, bike_model, quantity, wholesale_price):
        self.inventory[model]={quantity:wholesale_price}
        return self.inventory
    def sell_bike (self, model, production_cost):
        self.inventory[model]-=1
        self.profit+=production_cost*self.markup

class customers(object):
    def __init__(self, customer_name, budget, bikes_owned):
        customers.customer_name=customer_name
        customers.budget=budget
        customers.bikes_owned=bikes_owned
    def enter_store(self):
        shoppers.append(self.customer_name)
    def buy_bike(self, model, retail_price):
        customers.bikes_owned.append(model)
        customers.budget-=int(retail_price)


for bike in bicycles:
    print(bike.model)

    