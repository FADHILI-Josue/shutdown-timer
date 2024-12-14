import argparse
import time
import os
import platform


def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"Time remaining: {mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up! Shutting down the system.")
    
def shutdown_system():
    current_platform = platform.system()
    try:
        if current_platform == "Windows":
            os.system("shutdown /s /t 0")
        elif current_platform == "Linux":
            os.system("shutdown now")
        elif current_platform == "Darwin":
            os.system("sudo shutdown -h now")
        else:
            print(f"Shutdown is not supported on this platform: {current_platform}")
    except Exception as e:
        print(f"An error occurred while shutting down: {e}")

def schedule_shutdown(minutes):
    countdown(minutes)
    shutdown_system()

def main():
    parser = argparse.ArgumentParser(description="Schedule a PC shutdown.")
    parser.add_argument(
        "-m", "--minutes", type=int, default=30,
        help="Number of minutes to wait before shutting down. Default is 30 minutes."
    )
    args = parser.parse_args()
    minutes = args.minutes
    print(f"PC will shut down in {minutes} minutes. Press Ctrl+C to cancel.")
    try:
        schedule_shutdown(minutes)
    except KeyboardInterrupt:
        print("\nShutdown canceled by user.")

if __name__ == "__main__":
    main()
