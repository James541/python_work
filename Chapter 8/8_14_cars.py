def make_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

made_car = make_car('BMW', '7 Series', color='black', year='2023')

print(made_car)