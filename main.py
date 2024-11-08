import sys
import time
import board
import busio
import adafruit_ds3231
from datetime import datetime


def Read_time():
    # Setup I2C interface
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize the RTC
    rtc = adafruit_ds3231.DS3231(i2c)

    # Reading the time from DS3231
    t = rtc.datetime
    print("Current time: {}-{}-{} {}:{}:{}".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))


def Setting_time_from_input():
    # Get time input from user
    user_input = input("Enter the time (YYYY-MM-DD HH:MM:SS): ").strip()
    try:
        dt = datetime.strptime(user_input, '%Y-%m-%d %H:%M:%S')
        
        # Setup I2C interface
        i2c = busio.I2C(board.SCL, board.SDA)

        # Initialize the RTC
        rtc = adafruit_ds3231.DS3231(i2c)

        # Set the RTC time
        rtc.datetime = time.struct_time((dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, 0, -1, -1))

        print(f"Time set to {user_input} from user input.")
    except ValueError:
        print("Error: Invalid date format. Please enter in the format YYYY-MM-DD HH:MM:SS")


def Setting_time_to_now():
    # Get current system time
    now = datetime.now()

    # Setup I2C interface
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize the RTC
    rtc = adafruit_ds3231.DS3231(i2c)

    # Set the RTC time to current system time
    rtc.datetime = time.struct_time((now.year, now.month, now.day, now.hour, now.minute, now.second, 0, -1, -1))

    print(f"Time set to current system time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [Read | Setting | SetNow]")
        sys.exit(1)
    
    switch = sys.argv[1]
    if switch == "Read":
        Read_time()
    elif switch == 'Setting':
        Setting_time_from_input()  # User input option
    elif switch == 'SetNow':
        Setting_time_to_now()      # Set current system time option
    else:
        print("Invalid option. Use 'Read', 'Setting', or 'SetNow'.")
