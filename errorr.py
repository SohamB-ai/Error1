import random
import string
from datetime import datetime

def random_text(size=500):
    return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=size))

def generate_large_log(filename="huge_error.log", lines=1_000_000):
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(lines):
            log_line = (
                f"{datetime.now().isoformat()} - ERROR - Module{i%50} - "
                f"Failure occurred due to unexpected condition in processing pipeline, "
                f"caused by invalid state transition, memory overflow, race condition, "
                f"and corrupted input stream; details: {random_text(800)}; "
                f"traceback: Exception('critical failure at iteration {i}')\n"
            )
            f.write(log_line)

            # Optional: progress indicator
            if i % 100000 == 0:
                print(f"{i} lines written...")

    print("File generation complete.")

# Adjust lines to control file size
generate_large_log(lines=1_000_000)