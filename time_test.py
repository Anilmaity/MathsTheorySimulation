import time

# Record the start time
start_time = time.time()

# Loop 10,000 times
for _ in range(1000000):
    print("Hello, World!")

# Record the end time
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")
