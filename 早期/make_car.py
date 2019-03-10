def made_car(subrru_o,outback_o,**car_info):
    car_id = {}
    car_id['name'] = subrru_o
    car_id['color'] = outback_o
    for key,value in car_info.items():
        car_id[key] = value
    return car_id
new_car = made_car('subaru','outback',yanse='blue',two_package='True')
print(new_car)