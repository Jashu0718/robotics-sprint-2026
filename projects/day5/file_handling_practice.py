# Day 5 - Topic 4: File Handling + Realistic Error Handling

import datetime

def save_robot_log(robot_name, battery, position):
    try:
        with open("robot_log.txt", "a") as file:
            log = f"{robot_name} | Battery: {battery}% | Position: {position} | Time: {datetime.datetime.now().strftime('%H:%M:%S')}\n"
            file.write(log)
        print(f"✅ Log saved for {robot_name}")
    except Exception as e:
        print(f"❌ Error saving log: {e}")

def read_robot_logs():
    try:
        with open("robot_log.txt", "r") as file:
            print("\n📄 Robot Logs:\n")
            print(file.read())
    except FileNotFoundError:
        print("❌ No log file found yet.")
    except Exception as e:
        print(f"❌ Error reading logs: {e}")


if __name__ == "__main__":
    print("🚀 Day 5 - Topic 4 Practice\n")
    save_robot_log("JASHBOT-001", 85, (10, 15))
    save_robot_log("JASHBOT-002", 42, (25, 30))
    save_robot_log("JASHBOT-003", 95, (5, 8))
    read_robot_logs()
    print("\n🎯 Topic 4 Complete!")