import argparse
import time
import os

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"Time remaining: {mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up! Shutting down the system.")

def schedule_shutdown(minutes):
    countdown(minutes)
    os.system("shutdown /s /t 0")  # Shutdown command for Windows if using linux based os you may change it

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
