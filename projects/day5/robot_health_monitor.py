# Day 5 Evening - Robot Health Monitor (Advanced OOP + File Handling)

import datetime

class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self._battery = battery

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if 0 <= value <= 100:
            self._battery = value
        else:
            print("❌ Invalid battery level!")

    def status(self):
        return f"{self.name} | Battery: {self.battery}%"

class HealthMonitor:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)
        print(f"✅ Added {robot.name} to health monitor")

    def check_all(self):
        print("\n🔍 Robot Health Report")
        for robot in self.robots:
            print(robot.status())

    def save_report(self):
        try:
            with open("health_report.txt", "w") as f:
                f.write(f"Robot Health Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                f.write("="*50 + "\n")
                for robot in self.robots:
                    f.write(robot.status() + "\n")
            print("✅ Health report saved to health_report.txt")
        except Exception as e:
            print(f"❌ Error saving report: {e}")


# === Run the Health Monitor ===
if __name__ == "__main__":
    monitor = HealthMonitor()

    bot1 = Robot("JASHBOT-001", 85)
    bot2 = Robot("JASHBOT-002", 42)
    bot3 = Robot("JASHBOT-003", 95)

    monitor.add_robot(bot1)
    monitor.add_robot(bot2)
    monitor.add_robot(bot3)

    monitor.check_all()
    monitor.save_report()

    print("\n🎯 Day 5 Evening Project Complete!")