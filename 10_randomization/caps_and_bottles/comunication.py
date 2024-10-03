import subprocess
import threading
import time
import sys
from queue import Queue, Empty

path_to_script = "child.py"

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

def non_blocking_communicate(proc, inputs):
    output_queue = Queue()

    # Start a thread to read stdout
    thread = threading.Thread(target=enqueue_output, args=(proc.stdout, output_queue))
    thread.daemon = True
    thread.start()

    for input_data in inputs:
        # Wait for the prompt "What's your name?"
        while True:
            try:
                line = output_queue.get_nowait()  # Non-blocking get
            except Empty:
                time.sleep(0.01)  # Small delay before retrying
                continue  # No output yet, continue waiting for prompt
            else:
                line_decoded = line.decode()
                print(f"Proceso hijo dice: {repr(line_decoded)}")

                # When we see "What's your name?", we can send the next name
                if "What's your name?" in line_decoded:
                    proc.stdin.write(input_data)
                    proc.stdin.flush()
                    break

    proc.stdin.close()

    # Process remaining output after all inputs are sent
    while not output_queue.empty() or proc.poll() is None:
        try:
            line = output_queue.get_nowait()
            yield line.decode()
        except Empty:
            time.sleep(0.01)  # Give some time for the remaining output to appear

    proc.wait()
    thread.join()

cmd = [sys.executable, path_to_script]
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def generate_inputs():
    names = ["Aldo", "Briggit", "Silvia", "Marly", "exit"]
    for name in names:
        yield '{}\n'.format(name).encode()
        time.sleep(0.01)

for line in non_blocking_communicate(proc, generate_inputs()):
    print(f"Proceso hijo dice: {repr(line)}")
