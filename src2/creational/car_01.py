from car import Car, Wheel, Engine, Body


if __name__ == '__main__':
    # Type, Body, HP, tire size
    #
    # Jeep: SUV, 400, 22
    # Nissan: hatchback, 100, 16

    #  # You can also parametrize the code using
    # type_of_car = {
    #     'Jeep': {'body': 'SUV', 'hp': 400, 'wheel_size': 22},
    #     'Nissan': {'body': 'hatchback', 'hp': 100, 'wheel_size': 16}
    # }

    jeep = Car()
    body = Body('SUV')
    jeep.set_body(body)
    engine = Engine(400)
    jeep.set_engine(engine)

    for _ in range(4):
        wheel = Wheel(22)
        jeep.attach_wheel(wheel)

    nissan = Car()
    body = Body('hatchback')
    nissan.set_body(body)
    engine = Engine(100)
    nissan.set_engine(engine)

    for _ in range(4):
        wheel = Wheel(16)
    nissan.attach_wheel(wheel)

    print(jeep)
    jeep.specification()

    print(nissan)
    nissan.specification()

