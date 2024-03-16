import os

def stress_cpu(percentage):
    # calculate the number of cores
    num_cores = os.cpu_count()
    
    # calculate the number of processes based on the percentage
    num_processes = int(percentage / 100 * num_cores)

    # stress the CPU by running stress-ng command
    os.system(f"stress-ng --cpu {num_processes} --timeout 60s")

# Get user input for the desired CPU stress percentage
user_input = int(input("Enter the CPU stress percentage (25, 50, 75, 100): "))

# Perform CPU stress test based on user input
if user_input == 25:
    stress_cpu(25)
elif user_input == 50:
    stress_cpu(50)
elif user_input == 75:
    stress_cpu(75)
elif user_input == 100:
    stress_cpu(100)
else:
    print("Invalid input. Please enter 25, 50, 75, or 100.")
