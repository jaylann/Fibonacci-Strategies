import time
import gmpy2





# Timing the functions
def time_function(func, n):
    start_time = time.time()
    for i in range(n+1):
        func(100000000)
    end_time = time.time()
    return (end_time - start_time) / n

# Number of iterations
n = 1

# Timing the original function
#time_original = time_function(mat_fib, n)

# Timing the mpz function
time_mpz = time_function(mat_fib_mpz, n)

print(f"mpz function: {time_mpz}")
