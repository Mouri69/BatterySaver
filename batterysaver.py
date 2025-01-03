import psutil
import time
import tkinter as tk
from tkinter import messagebox
import winsound
import threading
from PIL import Image
import pystray

class BatterySaver:
    def __init__(self):
        # Create system tray icon first
        self.icon = self.create_tray_icon()
        self.is_running = True

    def create_tray_icon(self):
        # Create a simple image for the tray icon
        image = Image.new('RGB', (64, 64), color='green')  # Changed to green for better visibility
        icon = pystray.Icon(
            "BatterySaver",
            image,
            "Battery Saver Monitor",  # Hover text
            menu=pystray.Menu(
                pystray.MenuItem("Exit", self.quit_app)
            )
        )
        return icon

    def check_battery(self):
        while self.is_running:
            battery = psutil.sensors_battery()
            if battery.power_plugged and battery.percent >= 95:
                winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo(
                    "Battery Alert",
                    "Battery is fully charged! You can unplug your charger now."
                )
                root.destroy()
            time.sleep(300)

    def quit_app(self):
        self.is_running = False
        self.icon.stop()

    def run(self):
        # Start battery monitoring in a separate thread
        monitor_thread = threading.Thread(target=self.check_battery)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        # Run the system tray icon
        self.icon.run()

if __name__ == "__main__":
    app = BatterySaver()
    app.run()
