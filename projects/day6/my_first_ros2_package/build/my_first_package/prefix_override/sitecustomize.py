import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jashdynamics/robotics-sprint-2026/projects/day6/my_first_ros2_package/install/my_first_package'
