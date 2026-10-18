# Program 1: Online Load Balancing Across Multiple Processors

def online_load_balancing():
    print("\n--- Online Load Balancing ---")

    n = int(input("Enter number of processors: "))
    m = int(input("Enter number of jobs: "))

    if n <= 0 or m <= 0:
        print("Processors and jobs must be greater than zero.")
        return

    processors = [0] * n

    for i in range(m):
        job_time = int(input(f"Enter processing time for job {i + 1}: "))

        if job_time < 0:
            print("Processing time cannot be negative.")
            return

        min_processor = processors.index(min(processors))
        processors[min_processor] += job_time

        print(f"Job {i + 1} assigned to Processor {min_processor + 1}")

    print("\nFinal processor workloads:")

    for i in range(n):
        print(f"Processor {i + 1}: {processors[i]}")

    print("Maximum workload:", max(processors))


if __name__ == "__main__":
    online_load_balancing()