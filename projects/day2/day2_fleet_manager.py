import datetime
import random
import json
import csv
from dataclasses import dataclass

@dataclass
class RobotTelemetry:
    timestamp: str
    robot_id: str
    position: dict
    velocity: float
    battery: int
    status: str

class FleetManager:
    def __init__(self):
        self.robots = {}   # dictionary to store multiple loggers

    def add_robot(self, robot_id: str):
        """Add a new robot to the fleet"""
        self.robots[robot_id] = []
        print(f"✅ Added robot: {robot_id}")

    def log_robot_data(self, robot_id: str):
        """Log one reading for a specific robot"""
        if robot_id not in self.robots:
            print(f"❌ Robot {robot_id} not found!")
            return

        telemetry = RobotTelemetry(
            timestamp=datetime.datetime.now().isoformat(),
            robot_id=robot_id,
            position={"x": round(random.uniform(0, 100), 2), "y": round(random.uniform(0, 100), 2)},
            velocity=round(random.uniform(0, 5), 2),
            battery=random.randint(10, 100),
            status=random.choice(["Moving", "Idle", "Charging", "Error"])
        )
        
        self.robots[robot_id].append(telemetry.__dict__)
        print(f"📍 Logged data for {robot_id}")

    def save_all_data(self):
        """Save fleet data to JSON and CSV"""
        # Save as JSON
        with open("fleet_data.json", "w") as f:
            json.dump(self.robots, f, indent=2)
        
        # Save as CSV (simple version)
        with open("fleet_data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Robot ID", "Timestamp", "X", "Y", "Velocity", "Battery", "Status"])
            for robot_id, logs in self.robots.items():
                for log in logs:
                    writer.writerow([
                        robot_id,
                        log["timestamp"],
                        log["position"]["x"],
                        log["position"]["y"],
                        log["velocity"],
                        log["battery"],
                        log["status"]
                    ])
        
        print("✅ Fleet data saved to fleet_data.json and fleet_data.csv")
    def get_latest_status(self, robot_id: str):
        try:
            if robot_id not in self.robots or not self.robots[robot_id]:
                raise ValueError(f"Robot {robot_id} has no data yet")
            latest = self.robots[robot_id][-1]
            return f"{robot_id} is {latest['status']} | Battery: {latest['battery']}%"
        except Exception as e:
            return f"Error checking {robot_id}: {e}"
# === RUN THE FLEET MANAGER ===
if __name__ == "__main__":
    fleet = FleetManager()
    
    print("🚀 ROBOTICS SPRINT 2026 - DAY 2 STARTED\n")
    
    # Add 3 robots
    fleet.add_robot("JASHBOT-001")
    fleet.add_robot("JASHBOT-002")
    fleet.add_robot("JASHBOT-003")
    
    # Log data for each robot
    for _ in range(5):
        fleet.log_robot_data("JASHBOT-001")
        fleet.log_robot_data("JASHBOT-002")
    
    fleet.save_all_data()
    print(fleet.get_latest_status("JASHBOT-001"))
    print(fleet.get_latest_status("JASHBOT-002"))
    print("\n🎯 Day 2 complete! You now have a working Fleet Manager.")