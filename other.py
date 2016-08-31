schwinn=bicycle("schwinn", 100, 20)
schwinn.new_model()
speedster=bicycle("speedster", 120, 15)
speedster.new_model()
trek=bicycle("trek", 150, 12)
trek.new_model()
giant=bicycle("giant", 500, 8)
giant.new_model()
fuji=bicycle("fuji", 750, 13)
fuji.new_model()
kona=bicycle("kona", 300, 22)
kona.new_model()

sally=customers("sally", 200, [])
sally.enter_store()
jim=customers("Jim", 500, [])
jim.enter_store()
jane=customers("Jane", 1000, [])
jane.enter_store()

toms_store=bike_shop("toms", {} , 1.20, 0 )

for bikes in bicycles:
    toms_store.purchase_inventory(bikes, 50, bikes.production_cost)



print(toms_store.inventory)


