class User:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

    def race_mode(self):
        self.speed = 150


user_1 = User(89, 56)
print(user_1.speed)

user_2 = User(79, 9) 

print(user_1.speed and user_2.fuel)

user_2.race_mode()
print(user_2.speed)
