from memory_profiler import memory_usage
from src.q1_memory import q1_memory
from src.q2_memory import q2_memory
from src.q3_memory import q3_memory
from src.q1_time import q1_time
from src.q2_time import q2_time
from src.q3_time import q3_time

def measure_memory(func, *args, **kwargs):
    """
    Measures the memory usage of a function.
    """
    mem_usage = memory_usage((func, args, kwargs))
    result = func(*args, **kwargs)
    return result, max(mem_usage)  # Returning the result and max memory used

if __name__ == "__main__":
    file_path = "tweets.json/farmers-protest-tweets-2021-2-4.json"
    result, mem_used = measure_memory(q2_time, file_path)
    print(f"q2_memory result: {result}")
    print(f"Memory used: {mem_used} MB")
    
    