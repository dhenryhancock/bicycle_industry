class bicycle(object):
    def __init__(self, model, production_cost, weight):
        self.model=model
        self.production_cost=production_cost
        self.weight=weight

bicycles=[bicycle("schwinn", 100, 20), bicycle("speedster", 120, 15)]

class bike_shop(object):
    def __init__(self, store_name, markup):
        self.store_name=store_name
        self.markup=markup
    def purchase_inventory(self):
        self.inventory={}
        self.inventory_prices={}
        for bike in bicycles:
            bike_price=bike.production_cost * self.markup
            self.inventory[bike]=50
            self.inventory_prices[bike]=bike_price
    def available_bikes (self):
        for shopper in shoppers:
            print("Here are the bikes that {} can afford" .format(shopper.customer_name))
            for key in self.inventory:
                if self.inventory_prices[key] <= shopper.budget:
                    print (key)
                else:
                    pass

class customers(object):
    def __init__(self, customer_name, budget, bikes_owned):
        self.customer_name=customer_name
        self.budget=budget
        self.bikes_owned=bikes_owned
  
toms_store=bike_shop("toms_store", 1.25)

shoppers=[customers("Sally", 200, []), customers("Jim", 500, []), customers("Jane", 1000, [])]


toms_store.purchase_inventory()

print(toms_store.inventory)
print(toms_store.inventory_prices)

toms_store.available_bikes()