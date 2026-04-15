import datetime
import json
from dataclasses import dataclass

@dataclass
class Task:
    task_id: int
    title: str
    deadline: str
    priority: str
    status: str

class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.task_counter = 1

    def add_task(self, title: str, deadline: str, priority: str = "Medium"):
        """Add a new task to the scheduler"""
        task = Task(self.task_counter, title, deadline, priority, "Pending")
        self.tasks.append(task.__dict__)
        print(f"✅ Task added: {title} (ID: {self.task_counter})")
        self.task_counter += 1

    def show_tasks(self):
        """Display all tasks"""
        print("\n📋 Current Tasks:")
        for task in self.tasks:
            print(f"   {task['task_id']}. {task['title']} | Deadline: {task['deadline']} | Priority: {task['priority']} | Status: {task['status']}")

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f, indent=2)
        print("✅ All tasks saved to tasks.json")

# === RUN THE TASK SCHEDULER BOT ===
if __name__ == "__main__":
    print("🚀 Robotics Sprint 2026 - Day 4 Mini Project: Task Scheduler Bot\n")
    
    scheduler = TaskScheduler()
    
    # Add some sample tasks
    scheduler.add_task("Finish ROS2 installation", "2026-04-20", "High")
    scheduler.add_task("Complete Fiverr gigs", "2026-04-17", "High")
    scheduler.add_task("Study Navigation Stack", "2026-04-22", "Medium")
    scheduler.add_task("Prepare LinkedIn profile", "2026-04-18", "Medium")
    
    scheduler.show_tasks()
    scheduler.save_tasks()
    
    print("\n🎯 Day 4 Mini Project Complete! Task Scheduler Bot is ready.")