# Battery Saver Monitor

A Windows application that monitors your laptop's battery and alerts you when it's fully charged to prevent overcharging and optimize battery life.

## Features

- 🔋 Real-time battery monitoring
- 🔔 Sound and visual alerts when battery is fully charged (≥95%)
- 💻 Runs in system tray (minimized)
- 🚀 Automatic startup with Windows
- 🖥️ User-friendly interface

## Installation

### Method 1: Using the Executable
1. Download the latest release from the [Releases](link-to-releases) page
2. Run `Battery Saver.exe`
3. The application will start automatically and appear in your system tray

### Method 2: From Source
1. Clone this repository
```
git clone https://github.com/your-username/battery-saver.git
```
2. Install required dependencies

```
pip install psutil pillow pystray pywin32
```


## Usage

- The application runs in the system tray (bottom-right corner of the taskbar)
- When your battery reaches 95% while charging, you'll receive:
  - A sound alert
  - A popup notification
- Right-click the system tray icon to access options or exit

## Requirements

- Windows OS
- Python 3.6 or higher (if running from source)
- Required Python packages (if running from source):
  - psutil
  - pillow
  - pystray
  - pywin32

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using Python and various open-source libraries
- Inspired by the need to maintain battery health

## Support

If you encounter any problems or have suggestions, please open an issue on the GitHub repository.


