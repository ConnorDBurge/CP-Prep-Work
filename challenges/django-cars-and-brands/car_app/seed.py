from cars_and_brands.models import Car, Brand

brand1 = Brand(brand_name='Ford')
brand1.save()
brand1_models = ['Ranger', 'Bronco', 'Fusion', 'Mustang',
                 'Explorer', 'Escape', 'F150', 'F250', 'F350']
for model in brand1_models:
    car = Car(car_model=model, car_brand=brand1)
    car.save()

brand2 = Brand(brand_name='Toyota')
brand2.save()
brand2_models = ['Tacoma', 'Tundra', '4Runner', 'Camry',
                 'Avalon', 'FJ Cruiser', 'Highlander', 'Prius', 'Sequoia', 'Supra', 'Rav4', 'Corolla']
for model in brand2_models:
    car = Car(car_model=model, car_brand=brand2)
    car.save()


brand3 = Brand(brand_name='Honda')
brand3.save()
brand3_models = ['Accord', 'Civic', 'CR-V', 'Fit',
                 'Pilot', 'Insight', 'Odyssey', 'Ridgeline']
for model in brand3_models:
    car = Car(car_model=model, car_brand=brand3)
    car.save()
