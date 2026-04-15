import datetime
import random
import json
from dataclasses import dataclass

@dataclass
class RobotTelemetry:
    timestamp: str
    robot_id: str
    position: dict
    velocity: float
    battery: int
    status: str

class TelemetryLogger:
    def __init__(self, robot_id: str):
        self.robot_id = robot_id
        self.logs = []

    def log_data(self):
        telemetry = RobotTelemetry(
            timestamp=datetime.datetime.now().isoformat(),
            robot_id=self.robot_id,
            position={
                "x": round(random.uniform(0, 100), 2),
                "y": round(random.uniform(0, 100), 2),
                "z": 0.0
            },
            velocity=round(random.uniform(0, 5), 2),
            battery=random.randint(10, 100),
            status=random.choice(["Moving", "Idle", "Charging", "Error"])
        )
        self.logs.append(telemetry.__dict__)
        print(f"[{telemetry.timestamp}] Logged for {self.robot_id}")

    def save_to_file(self, filename: str = "telemetry_log.json"):
        with open(filename, "w") as f:
            json.dump(self.logs, f, indent=2)
        print(f"✅ Saved {len(self.logs)} logs to {filename}")

# === RUN IT ===
if __name__ == "__main__":
    logger = TelemetryLogger(robot_id="JASHBOT-001")
    
    print("🚀 ROBOTICS SPRINT 2026 - DAY 1 STARTED\n")
    for i in range(15):          # Log 15 readings
        logger.log_data()
    
    logger.save_to_file()
    print("\n🎯 Day 1 complete! First foundation built and saved.")