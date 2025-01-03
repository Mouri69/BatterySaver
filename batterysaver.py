import psutil
import time
import tkinter as tk
from tkinter import messagebox
import winsound
import threading

class BatterySaver:
    def __init__(self):
        self.is_running = True
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window
        
    def check_battery(self):
        while self.is_running:
            battery = psutil.sensors_battery()
            
            if battery.power_plugged and battery.percent >= 95:
                # Play alert sound
                winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
                
                # Show message box
                messagebox.showinfo(
                    "Battery Alert",
                    "Battery is fully charged! You can unplug your charger now."
                )
            
            time.sleep(300)  # Check every 5 minutes

    def run(self):
        # Start battery monitoring in a separate thread
        monitor_thread = threading.Thread(target=self.check_battery)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        # Run the main window
        self.root.mainloop()

if __name__ == "__main__":
    app = BatterySaver()
    app.run()
