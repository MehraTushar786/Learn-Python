# 🎯 Build a Vehicle class with:
# Properties:
# name (str)

# speed (int, default 0)

# fuel_level (int, default 50)

# is_on (bool, default False)

# Methods:
# start() → if fuel_level > 0, set is_on = True

# accelerate() → if is_on, increase speed by 10

# stop() → set is_on = False, speed = 0

# __str__() → Print a summary of the vehicle state

# 🧠 Bonus Task (Inheritance):
# Create a new class Car that inherits from Vehicle

# Add one method: play_music() → print “Playing music…”



class Vehicle:
    def __init__(self,name = '',speed = 0,fuel_level = 50,is_on = False):
        self.name = name
        self.speed = speed
        self.fuel_Level = fuel_level
        self.is_on = is_on

    def __str__(self):
        return f"Vehicle: {self.name} | Speed: {self.speed} km/h | Fuel: {self.fuel_Level}L | Status: {self.is_on}"

    def start(self):
        if(self.fuel_Level > 0):
            self.is_on = True

    def accelerate(self):
        if(self.is_on):
            self.speed += 10

    def stop(self):
        if(self.is_on == True):
            self.is_on = False
        self.speed = 0



class Car(Vehicle):
    def play_music(self):
        print('Playing Music...')



v1 = Vehicle("Mustang")

print(v1)              # Should show: speed 0, fuel 50, status OFF
v1.accelerate()        # Should NOT work (vehicle is OFF)
v1.start()             # Should turn it ON
v1.accelerate()        # Should increase speed by 10
print(v1)              # Speed should now be 10, status ON
v1.stop()              # Should turn it OFF and speed to 0
print(v1)              # Speed should now be 0, status OFF



c1 = Car("BMW")

print(c1)              # Initial state
c1.start()             # Turn car ON
c1.accelerate()        # Increase speed
c1.play_music()        # Play music (extra method from Car)
print(c1)              # Updated state
c1.stop()              # Turn car OFF
