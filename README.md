# Data Engineer Challenge

## Project Overview
This project addresses three main tasks using two approaches: one optimized for time and the other optimized for memory. The goal is to process large datasets of tweets efficiently and draw insights from them.

## How to Run
1. Clone this repository: `git clone https://github.com/AllanAscencio/latam-challenge.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the Python files from the `challenge_de` folder or open and run `challenge.ipynb` for a detailed walkthrough.

## Challenge Breakdown
### Challenge 1: Top 10 Dates with the Most Tweets
- **q1_time**: Uses optimized time execution with efficient sorting.
- **q1_memory**: Reads file line-by-line to reduce memory usage.

### Challenge 2: Top 10 Emojis Used
- **q2_time**: Utilizes multiprocessing to quickly process tweets in parallel.
- **q2_memory**: Memory-friendly processing using line-by-line reading.

### Challenge 3: Top 10 Most Mentioned Users
- **q3_time**: Parallel processing for fast user mentions counting.
- **q3_memory**: A more memory-efficient approach without parallelism.

## Performance Comparison
### Time Optimization
- q1_time: X seconds
- q2_time: X seconds
- q3_time: X seconds

### Memory Optimization
- q1_memory: X MB
- q2_memory: X MB
- q3_memory: X MB

## Design Decisions
- **Modularity**: Each task is broken down into small, manageable functions that handle specific parts of the process.
- **Efficiency**: Time functions prioritize fast execution by leveraging multiprocessing. Memory functions focus on conserving RAM by reading the dataset in chunks.
- **Error Handling**: Each function handles edge cases and potential errors, such as missing data, malformed JSON, and missing fields.
- **Creative Approaches**: The use of parallel processing for time optimization is a key creative approach in this project.

## Future Improvements
- Exploring additional performance improvements with Cython or JIT compilation.
- Further reducing memory footprint using more advanced data structures like tries for emoji counting.

