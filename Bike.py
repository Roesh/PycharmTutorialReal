class Bike:
    def __init__(self):
        self.speed=0
        self.odometer=0
        self.time=0

    def say_state(self):
        print("SPEED. IS {} KPH!".format(self.speed))

    def accelerate(self):
        if self.speed >= 10:
            print("Too fast! I will DIEE")
        else:
            self.speed += 2

    def brake(self):
        if self.speed <=0:
            print("Negative breaking? Only on Lear jets bro")
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time


if __name__ == '__main__':
    my_bike = Bike
    print("I'm a bike! A very nice bike")
    while True:
        action = input("What will you do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_bike.accelerate()
        elif action == 'B':
            my_bike.brake()
        elif action == 'O':
            print("The bike has driven {} kilometers".format(my_bike.odometer))
        elif action == 'S':
            print("The bike's average speed was {} kph".format(my_bike.average_speed()))
        my_bike.step()
        my_bike.say_state()
