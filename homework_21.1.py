from datetime import datetime

def analyze_log(input_file, output_file):
    key = "Key TSTFEED0300|7E3E|0400"
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        prev_time = None
        for line in infile:
            if key in line:

                idx = line.find("Timestamp ")
                if idx == -1:
                    continue
                time_str = line[idx + 10:idx + 18]
                try:
                    current_time = datetime.strptime(time_str, "%H:%M:%S")
                except ValueError:
                    continue

                if prev_time:
                    delta = (current_time - prev_time).total_seconds()
                    if delta < 0:
                        delta += 86400
                    if 31 < delta < 33:
                        outfile.write(f"WARNING: {delta:.2f} seconds at {time_str}\n")
                    elif delta >= 33:
                        outfile.write(f"ERROR: {delta:.2f} seconds at {time_str}\n")
                prev_time = current_time

analyze_log("hblog.txt", "hb_test.log")