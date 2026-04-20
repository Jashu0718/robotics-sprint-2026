# Day 5 - Topic 3: Better OOP (Inheritance + Properties)

class Robot:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving")

class AdvancedRobot(Robot):
    def __init__(self, name, battery):
        super().__init__(name)
        self._battery = battery

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if 0 <= value <= 100:
            self._battery = value
        else:
            print("❌ Invalid battery level! Must be between 0 and 100.")

    def status(self):
        print(f"{self.name} has {self.battery}% battery")


if __name__ == "__main__":
    bot = AdvancedRobot("JASHBOT-001", 75)
    bot.move()
    print("Current Battery:", bot.battery)
    bot.battery = 90
    bot.status()
    bot.battery = 120   # This will trigger the error message
    bot.status()