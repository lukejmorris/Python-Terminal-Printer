"""
Author: Luke Morris

This class allows the creation of a thread that will print a string and then at 
set time intervals will print a '.'.

This class is designed to be used by a TerminalPrinter object to allow loading 
trackers to be used.

When creating the thread values can be provided for:
    - the string to be printed at the beginning of the loading tracker.
    - the time to pass before the string is printed. This delay allows the program
    calling the thread to complete and terminate the thread before printing if 
    the program completes quickly.
    - the time to pass between printing the dots for the loading tracker
    - the maximum time that the thread should remain alive. This makes sure that
    the thread will self terminate regardless of whether the programming creating
    this thread fails to terminate it.

Last modified: 22 January 2024
"""

import threading
import time

class LoadingThread(threading.Thread):

    def __init__(self, stop_event: threading.Event,
        starting_text: str = "Loading", 
        time_before_start: float = 0.25,
        time_between_dots: float = 0.5,
        max_time_alive: float = 120.0):

        super().__init__()
        self.__starting_text = starting_text
        self.__stop_event = stop_event
        self.__time_before_start = time_before_start
        self.__time_between_dots = time_between_dots
        self.__max_time_alive = max_time_alive

    def run(self):

        # pause for short period before starting to allow processing by application
        # before the starting text is used. Allows quick processing to
        # happen without the thread printing if finished quickly
        if self.__time_before_start > 0:
            time.sleep(self.__time_before_start)

        # print starting text if stop_event has not been received
        if not self.__stop_event.is_set():

            # set start time for thread
            start_time = time.time()

            # print starting text
            print(self.__starting_text, end='', flush=True)

            # set counter for paragraph width - max 80
            paragraph_width_ctr = len(self.__starting_text) % 80

            # print dots
            while not self.__stop_event.is_set():

                # set elapsed time
                elapsed_time = time.time() - start_time

                # break while loop if max time for thread to be active is not reached
                if elapsed_time >= self.__max_time_alive:

                    # set stop_event
                    self.__stop_event.set()

                    # break while loop
                    break

                # go to new line if paragraph width reached
                if paragraph_width_ctr >= 80:
                    print('') # go to new line
                
                # print dot
                print('.', end='', flush=True)
                
                # wait
                time.sleep(self.__time_between_dots)

                