# RedditPiCacher

## Description
RedditPiCacher is a Python application designed for fetching, storing, and caching Reddit posts. It's built to interface with Reddit's API, store data in MongoDB, and maintain a local JSON cache. This application can be run on various platforms, including Raspberry Pi.

This was a weekend project of mine designed to cache results if connection to a database could not be made.

## Installation

### Prerequisites
Ensure you have Python 3.x installed on your system. You can download it from [Python's official website](https://www.python.org/).

Ensure you have mongodb installed on your host system

### Dependencies
Install the necessary Python packages using pip:

```bash
pip install pymongo
pip install requests
pip install schedule
```

### Optional: Raspberry Pi Specific
If you're running this on a Raspberry Pi and wish to use the GPIO functionalities (e.g., LED blinking on errors), you need to install the gpiozero library:

```bash
pip install gpiozero
```
Note: The GPIO functionalities are optional and only required if running the application on a Raspberry Pi with hardware interface. Its only use is to blink a light when an error has occurred

### Usage
1. Clone the repo to your local machine:
    ```bash
    git clone https://github.com/Coder-Andrew/PiRedditCacher.git
    ```
2. Navigate to the cloned directory:
    ```bash
    cd RedditPiCacher
    ```
3. Run the script:
    ```bash
    python main.py
    ```

### Configuration
Before running the application, ensure to configure the database details, API endpoints, and any other specifics in the script.
