import json
from binary_heap import BinaryHeap

def load_json(path):
    intervals = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            intervals.append((
                int(obj['start']),
                int(obj['end']),
                obj['id']
            ))
    return intervals

def solve(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    heap = BinaryHeap()
    next_buffer = 1
    assignments = {}

    for start, end, res_id in sorted_intervals:
        if heap.size() > 0 and heap.peek()[0] <= start:
            old_end, buf_num = heap.replace_top((end, buf_num))
            assignments[res_id] = buf_num
        else:
            buf_num = next_buffer
            next_buffer += 1

            heap.push((end, buf_num))
            assignments[res_id] = buf_num

    total_buffers = next_buffer - 1
    result = [(res_id, assignments[res_id]) for start, end, res_id in sorted_intervals]
    return result, total_buffers
def solve_etalon(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    buffers = []
    next_buffer = 1
    assignments = {}

    for start, end, res_id in sorted_intervals:
        best_idx = -1
        best_end = 10**10
        best_num = 10**10

        for i in range(len(buffers)):
            buf_end, buf_num = buffers[i]
            if buf_end <= start:
                if (buf_end < best_end) or (buf_num < best_num and buf_end == best_end):
                    best_idx = i
                    best_end = buf_end
                    best_num = buf_num
        if best_idx != -1:
            buffers[best_idx] = (end, buffers[best_idx][1])
            assignments[res_id] = buffers[best_idx][1]
        else:
            buf_num = next_buffer
            next_buffer += 1
            buffers.append((end, buf_num))
            assignments[res_id] = buf_num
    total_buffers = next_buffer - 1

    result = [(res_id, assignments[res_id]) for start, end, res_id in sorted_intervals]

    return result, total_buffers

