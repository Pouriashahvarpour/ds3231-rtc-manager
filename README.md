
# DS3231 RTC Python Interface

This project allows you to read and set the time on a DS3231 Real-Time Clock (RTC) module using a Raspberry Pi 4B and Python. You can either read the current time stored in the RTC or set the time manually through user input or Setting time from OS system time.

## Requirements

1. **Hardware**:
   - Raspberry Pi 4B (or compatible model)
   - DS3231 RTC module
   - Jumper wires for connections

2. **Software**:
   - Python 3.x
   - Required Python libraries:
     - `adafruit-blinka`
     - `adafruit-circuitpython-ds3231`

  
## Wiring

| DS3231 Pin | Raspberry Pi Pin (GPIO) |
|------------|--------------------------|       
| VCC        | 3.3V (Pin 1)             |
| GND        | Ground (Pin 6)           |
| SDA        | SDA (Pin 3, GPIO 2)      |
| SCL        | SCL (Pin 5, GPIO 3)      |

## GPIO Pinout Table
| Pin | Name   | Pin | Name   |
|-----|--------|-----|--------|
| 1   | 3.3V   | 2   | 5V     |
| 3   | GPIO 2 (SDA1, I2C) | 4   | 5V     |
| 5   | GPIO 3 (SCL1, I2C) | 6   | GND    |
| 7   | GPIO 4 (GPCLK0)    | 8   | GPIO 14 (TXD0, UART) |
| 9   | GND    | 10  | GPIO 15 (RXD0, UART) |
| 11  | GPIO 17| 12  | GPIO 18 (PCM_CLK) |
| 13  | GPIO 27| 14  | GND    |
| 15  | GPIO 22| 16  | GPIO 23 |
| 17  | 3.3V   | 18  | GPIO 24 |
| 19  | GPIO 10 (MOSI, SPI) | 20  | GND    |
| 21  | GPIO 9 (MISO, SPI)  | 22  | GPIO 25 |
| 23  | GPIO 11 (SCLK, SPI) | 24  | GPIO 8 (CE0, SPI) |
| 25  | GND    | 26  | GPIO 7 (CE1, SPI) |
| 27  | ID_SD  | 28  | ID_SC  |
| 29  | GPIO 5 | 30  | GND    |
| 31  | GPIO 6 | 32  | GPIO 12 (PWM0) |
| 33  | GPIO 13 (PWM1) | 34  | GND    |
| 35  | GPIO 19 (PCM_FS) | 36  | GPIO 16 |
| 37  | GPIO 26 | 38  | GPIO 20 (PCM_DIN) |
| 39  | GND    | 40  | GPIO 21 (PCM_DOUT) |



## Installation

### 1. **Enable I2C on your system** (e.g., on a Raspberry Pi):
   - Run `sudo raspi-config`
   - Go to `Interface Options` and enable `I2C`.
   - Reboot the system if necessary.

### 2. **Clone this repository** to download the script:
   ```bash
   git clone https://github.com/Pouriashahvarpour/ds3231-rtc-manager.git
   ```
### 2. Install Required Python Libraries

Run the following commands to install the necessary Python libraries:
```bash
sudo apt-get install -y python3-smbus i2c-tools
```
### 3. Check Installation 
  - Run `i2cdetect -y 1` to check if the Raspberry Pi can detect the DS3231 RTC. You should see the device address (typically `0x68`).

```bash
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- 57 -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- -- 
```

### 4.  Environment preparation
#### 1. First move to project directory:
```bash
cd ~/Desktop/ds3231-rtc-manager/
```
#### 2. Make virtual environment
```bash
python3 -m venv env
```

#### 3. Move to VM
```bash
source env/bin/activate
```

#### 4. Install dependency Libraries
```bash
pip3 install -r requirements.txt
```


## Usage

1. To use the script, navigate to the directory where the script is located:

```bash
cd ~/Desktop/ds3231-rtc-manager/
```

2. The script `main.py` provides three main functions. Run it with one of the following options:

    ```bash
    python3 main.py [Read | Setting | SetNow]
    ```

   - **Reading the RTC time**:

     ```bash
     python3 main.py Read
     ```

     This will display the current time stored in the DS3231 RTC.

   - **Setting the RTC time via user input**:

     ```bash
     python3 main.py Setting
     ```

     The script will prompt you to enter the time in the format `YYYY-MM-DD HH:MM:SS`. For example:

     ```
     Enter the time (YYYY-MM-DD HH:MM:SS): 2024-10-21 10:00:00
     ```

    - **Set DS3231 to Current System Time**:
      ```bash
      python3 main.py SetNow
       ```
## Example

### Reading the RTC Time:
```bash
python3 main.py Read
```
**Output**:
```
Current time: 2024-10-21 10:00:00
```

### Setting the RTC Time via User Input:
```bash
python3 main.py Setting
```
**User Input**:
```
Enter the time (YYYY-MM-DD HH:MM:SS): 2024-10-21 10:00:00
```
**Output**:
```
Time set to 2024-10-21 10:00:00 from user input.
```

## Code Overview

- `Read_time()`: Reads the current time from the DS3231 RTC module.
- `Setting_time_from_input()`: Sets the RTC time based on a user-provided input.
- `Setting_time_to_now()`: Sets the RTC time to match the current system time.


## License

This project is licensed under the MIT License.

## Contact
For any questions or issues, please contact:



[![Gmail](https://skillicons.dev/icons?i=gmail)](pouria.shahvarpour@gmail.com) 
[![Linkedin](https://skillicons.dev/icons?i=linkedin)](https://ir.linkedin.com/in/pouriashavarpour)
[![Instagram](https://skillicons.dev/icons?i=instagram)](https://www.instagram.com/pouria_shahvarpour)



