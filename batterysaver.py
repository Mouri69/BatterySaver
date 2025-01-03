import psutil
import time
from plyer import notification

def check_battery():
    battery = psutil.sensors_battery()
    
    if battery.power_plugged and battery.percent >= 95:
        notification.notify(
            title="Battery Alert",
            message="Battery is fully charged! You can unplug your charger now.",
            app_icon=None,  # You can specify a custom icon path here
            timeout=10
        )

def main():
    print("Battery monitoring started...")
    while True:
        check_battery()
        time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    main()
