# python3

class Worker:

    def __init__(self, free_time, index):
        self.free_time = free_time
        self.index = index

    def __lt__(self, other):
        if self.free_time == other.free_time:
            return self.index < other.index
        else:
            return self.free_time < other.free_time

    def __eq__(self, other):
        return self.free_time == other.free_time and self.free_time == other.free_time


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.workers = [Worker(0, i-1) for i in range(self.num_workers+1)]
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def left(self, i):
        return i * 2

    def right(self, i):
        return i * 2 + 1

    def sift_down(self, i):
        min_index = i
        left_index, right_index = self.left(i), self.right(i)
        if left_index <= self.num_workers and self.workers[left_index] < self.workers[min_index]:
            min_index = left_index
        if right_index <= self.num_workers and self.workers[right_index] < self.workers[min_index]:
            min_index = right_index
        if min_index != i:
            self.workers[min_index], self.workers[i] = self.workers[i], self.workers[min_index]
            self.sift_down(min_index)

    def assign(self, p):
        self.workers[1].free_time += p
        self.sift_down(1)

    def assign_jobs(self):
        size = len(self.jobs)
        self.assigned_workers = [0 for i in range(size)]
        self.start_times = [0 for i in range(size)]
        for i in range(size):
            self.assigned_workers[i] = self.workers[1].index
            self.start_times[i] = self.workers[1].free_time
            self.assign(self.jobs[i])

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

