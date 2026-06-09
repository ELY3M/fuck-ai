import time
import sys

try:
    while True:
        # Fetch system time in standard format
        current_time = time.strftime('%I:%M:%S %p')
        
        # Print to the exact same line over and over
        sys.stdout.write(f"\rCurrent Time: {current_time}")
        sys.stdout.flush()
        
        # Pause for 1 second before refreshing
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")