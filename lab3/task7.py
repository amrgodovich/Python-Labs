import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        diff = end - start

        log = f"{func} executed in {diff:.4f} seconds\n"
        with open("execution_log.txt", "a") as f:
            f.write(log)

        print(f"{log.strip()}")
        return result
    return wrapper
