import matplotlib.pyplot as plt
import numpy as np

# Generate sample data for directional changes (random for demonstration)
directional_changes = np.random.rand(10, 2)
original_direction_changes = np.random.rand(10, 2)

# Compute average displacement vector
avg_displacement_vector = np.mean(np.diff(directional_changes, axis=0), axis=0)

# Calculate the time dilation factor using the Gott-Time Machine Metric
def gott_time_machine_metric(observer1, observer2):
    delta_x = observer1[0] - observer2[0]
    delta_y = observer1[1] - observer2[1]
    distance_squared = delta_x**2 + delta_y**2
    return np.sqrt(1 - distance_squared / (300**2))

# Set observer positions
observer1_position = directional_changes[0]
observer2_position = directional_changes[-1]

# Calculate the time dilation factor between the observers
time_dilation_factor = gott_time_machine_metric(observer1_position, observer2_position)

# Create figure and subplots
fig, axs = plt.subplots(2, 4, figsize=(20, 10))

# Plot original directional changes
axs[0, 0].plot(original_direction_changes[:, 0], original_direction_changes[:, 1], 'b--')
axs[0, 0].set_title('Original Directional Changes')
axs[0, 0].set_xlabel('X')
axs[0, 0].set_ylabel('Y')

# Plot directional changes
axs[0, 1].plot(directional_changes[:, 0], directional_changes[:, 1], 'b--')
axs[0, 1].set_title('Directional Changes')
axs[0, 1].set_xlabel('X')
axs[0, 1].set_ylabel('Y')

# Plot vertically arranged directional changes
axs[0, 2].plot(range(len(directional_changes)), directional_changes[:, 0], 'b--')
axs[0, 2].plot(range(len(directional_changes)), directional_changes[:, 1], 'r--')
axs[0, 2].set_title('Vertically Arranged Directional Changes')
axs[0, 2].set_xlabel('Index')
axs[0, 2].set_ylabel('Magnitude')

# Plot horizontally arranged directional changes
axs[0, 3].plot(directional_changes[:, 0], 'b--')
axs[0, 3].plot(directional_changes[:, 1], 'r--')
axs[0, 3].set_title('Horizontally Arranged Directional Changes')
axs[0, 3].set_xlabel('Index')
axs[0, 3].set_ylabel('Magnitude')

# Plot time invariance as a function of space
axs[1, 0].plot(directional_changes[:, 0] - avg_displacement_vector[0], 'b--')
axs[1, 0].plot(directional_changes[:, 1] - avg_displacement_vector[1], 'r--')
axs[1, 0].set_title('Time Invariance as Function of Space')
axs[1, 0].set_xlabel('Index')
axs[1, 0].set_ylabel('Magnitude')

# Plot time invariance as a function of time
axs[1, 1].plot(avg_displacement_vector[0], 'b--')
axs[1, 1].plot(avg_displacement_vector[1], 'r--')
axs[1, 1].set_title('Time Invariance as Function of Time')
axs[1, 1].set_xlabel('Index')
axs[1, 1].set_ylabel('Magnitude')

# Plot directional changes with arrow subplot
axs[1, 2].plot(directional_changes[:, 0], directional_changes[:, 1], 'b--')
axs[1, 2].arrow(directional_changes[-1, 0], directional_changes[-1, 1], 
                avg_displacement_vector[0], avg_displacement_vector[1], 
                head_width=0.1, head_length=0.1, fc='red', ec='red', linewidth=1)
axs[1, 2].set_title('Directional Changes with Heading Arrow')
axs[1, 2].set_xlabel('X')
axs[1, 2].set_ylabel('Y')

# Plot Gott-Time Equation
axs[1, 3].axis('off')
axs[1, 3].text(0.5, 0.5, f'Time Dilation Factor: {time_dilation_factor:.2f}', fontsize=12, ha='center')

plt.tight_layout()
plt.show()
