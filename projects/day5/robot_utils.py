# robot_utils.py - Helper module for robotics

def calculate_distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points"""
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def battery_status(level):
    """Return battery status as string"""
    if level > 70:
        return "High"
    elif level > 30:
        return "Medium"
    else:
        return "Low"