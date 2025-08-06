def make_car(model_name, manufacturer, **car_info):
    car = {}
    car['model_name'] = model_name
    car['manufacturer'] = manufacturer
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car("demio", "mazda", color="black", max_speed=240, year_model=2018)
print(car)
