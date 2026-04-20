# Day 5 - Topic 1: List Comprehensions + Lambda Functions

robots_battery = [85, 30, 65, 20, 90, 45, 75, 10, 55]

# List Comprehension examples
good_battery = [bat for bat in robots_battery if bat > 50]
doubled_battery = [bat * 2 for bat in robots_battery]
battery_status = ["High" if bat > 60 else "Low" for bat in robots_battery]

print("Good battery robots:", good_battery)
print("Doubled battery:", doubled_battery)
print("Battery status:", battery_status)

# Lambda functions
distance = lambda x1, y1, x2, y2: ((x2 - x1)**2 + (y2 - y1)**2)**0.5
battery_level = lambda level: "High" if level > 70 else "Medium" if level > 30 else "Low"

print("\nDistance between (0,0) and (10,15):", distance(0, 0, 10, 15))
print("Battery status of 45%:", battery_level(45))