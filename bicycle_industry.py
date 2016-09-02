import operator

class bicycle(object):
    def __init__(self, model, production_cost, weight):
        self.model=model
        self.production_cost=production_cost
        self.weight=weight

bicycles=[bicycle("schwinn", 100, 20), 
        bicycle("speedster", 120, 15), 
        bicycle("trek", 150, 12), 
        bicycle("giant", 500, 8), 
        bicycle("fuji", 750, 13), 
        bicycle("kona", 300, 22),]

class bike_shop(object):
    def __init__(self, store_name, markup, profit):
        self.store_name=store_name
        self.markup=markup
        self.profit=profit
    def purchase_inventory(self):
        self.inventory={}
        self.inventory_prices={}
        for bike in bicycles:
            bike_model=bike.model
            bike_price=bike.production_cost * self.markup
            self.inventory[bike_model]=50
            self.inventory_prices[bike_model]=bike_price
    def sell_bike (self):
        for people in customer_selections:
            selection=customer_selections[people]
            self.inventory[selection]-=1
            self.profit+=self.inventory_prices[selection]
        print (self.inventory)
        print (self.profit)

class customers(object):
    def __init__(self, customer_name, budget, affordable_bikes, bikes_owned):
        self.customer_name=customer_name
        self.budget=budget
        self.bikes_owned=bikes_owned
        self.affordable_bikes=affordable_bikes
    def check_price (self):
        self.affordable_bikes={}
        for store in stores:
            print("Here are the bikes that {} can afford" .format(self.customer_name))
            for bike in bicycles:
                if bike.production_cost*store.markup <= self.budget:
                    print (bike.model)
                    price=bike.production_cost*store.markup
                    print(price)
                    self.affordable_bikes[bike.model]=price
                else:
                    pass
            print(self.affordable_bikes)
    def buy_bike(self):
        selection=max(self.affordable_bikes, key=self.affordable_bikes.get)
        customer_selections[self.customer_name]=selection
        self.bikes_owned.append(selection)
        selection_price=self.affordable_bikes[selection]
        self.budget-=selection_price
        print("{0} now owns a {1}. Her remaining budget is ${2}." .format(self.customer_name, self.bikes_owned, self.budget))
  
stores=[bike_shop("toms_store", 1.25, 0)]

shoppers=[customers("Sally", 200, [], []), customers("Jim", 500, [], []), customers("Jane", 1000, [], [])]

customer_selections={}

for store in stores:
    store.purchase_inventory()

for shopper in shoppers:
    shopper.check_price()
    shopper.buy_bike()
    
for store in stores:
    store.sell_bike()
    