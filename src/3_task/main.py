import json
import sys
from ReusingBuffersDuringRendering import load_json, solve

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.json"
    try:
        intervals = load_json(input_file)

        result, total_buffers = solve(intervals)
        answer = {
            "Всего Буферов": total_buffers,
            "Этапы": [
                {"id": res_id, "буфер": buf_num}
                for res_id, buf_num in result
            ]
        }
        print(json.dumps(answer, ensure_ascii=False))
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()