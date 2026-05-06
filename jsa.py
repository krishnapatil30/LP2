# Job Scheduling Problem

def job_scheduling(jobs):
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]
    slots = [-1] * (max_deadline + 1)

    total_profit = 0

    for job_id, deadline, profit in jobs:
        # Find slot for this job
        for j in range(deadline, 0, -1):
            if slots[j] == -1:
                slots[j] = job_id
                total_profit += profit
                break

    return slots, total_profit


# (JobID, Deadline, Profit)
jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

schedule, profit = job_scheduling(jobs)

print("Job sequence:", schedule[1:])
print("Total Profit:", profit)