import math
import numpy as np
import matplotlib.pyplot as plt

# Constants for the Turtlebot's kinematics
WHEEL_RADIUS = 0.03  # meters
WHEEL_DISTANCE = 0.23  # meters

# Time interval for simulation
DELTA_T = 0.1  # seconds

def simulate_turtlebot(rpm_left, rpm_right, time):
    # Convert RPM values to radians per second
    omega_left = math.radians(rpm_left * 360 / 60)
    omega_right = math.radians(rpm_right * 360 / 60)

    # Calculate linear and angular velocities of the Turtlebot
    v = (WHEEL_RADIUS / 2) * (omega_left + omega_right)
    w = (WHEEL_RADIUS / WHEEL_DISTANCE) * (omega_right - omega_left)

    # Initialize the Turtlebot's position and orientation
    x = 0.0
    y = 0.0
    theta = 0.0

    # Simulate the Turtlebot's movement over time
    positions = [(x, y)]
    for t in np.arange(0.0, time, DELTA_T):
        x += v * math.cos(theta) * DELTA_T
        y += v * math.sin(theta) * DELTA_T
        theta += w * DELTA_T
        positions.append((x, y))

    # Return the final position and orientation
    return positions

# Define the actions
actions = [[0, 50], [50, 0], [50, 50], [0, 100], [100, 0], [100, 100], [50, 100], [100, 50]]

# Set the initial RPM values
rpm_left = 0
rpm_right = 0

# Initialize the Turtlebot's position and orientation
x = 0.0
y = 0.0
theta = 0.0

# Plot the initial position of the Turtlebot
plt.plot(x, y, 'ro')

# Simulate the Turtlebot's movement for each action and plot the trajectory
for action in actions:
    rpm_left, rpm_right = action
    positions = simulate_turtlebot(rpm_left, rpm_right, time=2.0)
    x, y = zip(*positions)
    plt.plot(x, y, 'b-')

    # Plot the final position of the Turtlebot for the current action
    plt.plot(x[-1], y[-1], 'go')

    # Reset the Turtlebot's position and orientation for the next action
    x, y, theta = positions[-1][0], positions[-1][1], 0.0

# Set the axis limits and labels
plt.xlim(0, 0.8)
plt.ylim(-0.35, 0.35)
plt.xlabel('X (m)')
plt.ylabel('Y (m)')

# Show the plot
plt.show()
