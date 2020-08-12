#! python3
# prettifiedStopwatch.py - Expand the stopwatch project from this
#                          chapter so that it uses the rjust() and
#                          ljust() string methods to “prettify” the
#                          output.
# Adam Pellot

import pyperclip
import time


# Display the program's instructions.
print('''Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.
Press Ctrl-C to quit.''')
input()                    # Press Enter to begin.
print('Started.')
startTime = time.time()    # Get the first lap's start time.
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
results = []
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        # "Prettified" variables for output.
        pLapNum = str(lapNum).rjust(2)
        pTotalTime = str(totalTime).rjust(6)
        pLapTime = str(lapTime).rjust(6)
        print('Lap #%s: %s (%s)' % (pLapNum, pTotalTime, pLapTime), end='')
        results.append('Lap #%s: %s (%s)' % (pLapNum, pTotalTime, pLapTime))
        lapNum += 1
        lastTime = time.time()  # Reset the last lap time.
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    # Copy results to clipboard via pyperclip.
    pyperclip.copy('\n'.join(results))
