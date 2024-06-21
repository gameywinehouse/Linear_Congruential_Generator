import time
import math
import threading

# Linear Congruential Generator (LCG) parameters
multiplier = 1664525
increment = 1013904223
modulus = 2**32

# Seed initialization with current time
initial_seed = int(time.time() * 1000) % modulus

# Random number generator using LCG
def custom_lcg(seed):
    euler_constant = math.exp(1) * 1000
    while True:
        seed = (multiplier * seed + increment) % modulus
        # Modify the seed using Euler's number and a trigonometric function
        adjusted_seed = (seed + int(euler_constant) + int(math.sin(seed) * 1000)) % modulus
        # Yield a normalized random number
        yield adjusted_seed / modulus

# Generator instance
random_number_generator = custom_lcg(initial_seed)

# Function to produce random numbers
def produce_random_numbers(stop_signal):
    while not stop_signal.is_set():
        print(next(random_number_generator))
        time.sleep(1)  # Generate a new number every second

# Create a stop signal
stop_signal = threading.Event()

# Start the random number generator in a new thread
random_thread = threading.Thread(target=produce_random_numbers, args=(stop_signal,))
random_thread.start()

# Function to stop the generator
def terminate_generator():
    stop_signal.set()
    random_thread.join()

# Wait for the user to press Enter to stop the generator
input("Press Enter to stop the generator...\n")
terminate_generator()
