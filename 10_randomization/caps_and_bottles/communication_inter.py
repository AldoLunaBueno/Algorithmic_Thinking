import subprocess
import threading
import time
import sys
from queue import Queue, Empty

class Communication:
    """
    A class to handle non-blocking communication with a child process using stdin and stdout.

    This class creates a subprocess, reads the child process's output using a separate thread, 
    and allows sending input and retrieving output in a non-blocking manner. It supports context 
    management for automatic resource cleanup (i.e., closing stdin, waiting for process termination, 
    and joining threads).

    Methods:
        isfinish(): Checks if the child process has finished execution.
        write(): Sends input to the child process via stdin.
        read(): Reads output from the child process's stdout in a non-blocking manner.
    """
    def __init__(self, child_script: str):
        """
        Initializes the Communication instance by launching the child process and starting
        a thread to read its stdout.

        Args:
            child_script (str): Path to the child script to be executed by the subprocess.
        """
        self._delay = 0.00001
        cmd = [sys.executable, "-u", child_script] # unbuffered mode
        self._proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._output_lines = Queue()

        # Start a thread to read stdout
        self._thread = threading.Thread(target=self._enqueue_output, args=(self._proc.stdout, self._output_lines))
        self._thread.daemon = True
        self._thread.start()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._proc.stdin.close()
        self._proc.wait()
        self._thread.join()
        return exc_type is None

    def _enqueue_output(self, out, queue):
        for line in iter(out.readline, b''):
            queue.put(line)
        out.close()

    def isfinish(self) -> bool:
        """
        Checks if the child process has finished execution.

        Returns:
            bool: True if the process has finished, False otherwise.
        """
        return self._proc.poll() is not None

    def write(self, input_data: str):
        """
        Sends input to the child process's stdin.

        This method writes the provided data to the child process's stdin, appends a newline,
        flushes the input stream, and waits for the specified delay.

        Args:
            input_data: The input string to send to the child process.
        """
        input_data = f"{input_data}\n".encode()
        self._proc.stdin.write(input_data)
        self._proc.stdin.flush()
        time.sleep(self._delay)

    def read(self) -> str|None:
        """
        Reads a line of output from the child process's stdout in a non-blocking manner.

        This method checks for output in the queue and retrieves a line if available.
        It continues retrying until either output is available or the process finishes.

        Returns:
            str | None: The decoded output string from the child process, or None if no output was found.
        """
        line_decoded = None
        while not self.isfinish():
            try:
                line = self._output_lines.get_nowait()  # Non-blocking get
            except Empty:
                time.sleep(self._delay)  # Small delay before retrying
                continue  # No output yet, continue waiting for prompt
            line_decoded = line.decode().strip()
            break
        return line_decoded