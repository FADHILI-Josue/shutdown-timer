# 💤 Auto Shutdown Timer 🕒

Just a simple Python script to shut down your PC after a set time. Think of it as a sleep timer for your computer 😴.

## Tired of This Scenario?  
You're lying in bed, listening to your favorite music, and somewhere between *track 5* and *dreamland*, you fall asleep. Fast forward to the morning, and you wake up to:  
- A **completely drained battery**.  
- A **powered-off PC**.  


## Installation  

### 1. Clone the Repo  
```bash
git clone https://github.com/FADHILI-Josue/shutdown-timer.git
cd shutdown-timer
```

### 2. Run the Script  
```bash
python shutdown_timer.py -m 15
```
- Shuts down your PC in 15 minutes.  
- Skip `-m` for the default 30-minute timer.  

### 3. (Optional) Create an Executable  
Want it as a global command sim(short for *Shutdown in Minutes*)? Follow these steps:  
1. Install `pyinstaller`:  
   ```bash
   pip install pyinstaller
   ```
2. Bundle the script into an executable:  
   ```bash
   pyinstaller --onefile shutdown_timer.py -n sim
   ```
3. Move the `sim.exe` to the folder where you store your cli tools and add the path to `sim.exe` to the environment variables in system’s PATH for easy access.  

4. open cmd and run sim as global cli 
```bash
sim -m 20
```


## How to Use  
1. **Run the Script**  
   Use the command below to start the countdown:  
   ```bash
   sim -m 20
   ```
   This will shut down your PC after 20 minutes.  

   Or, let it default to 30 minutes:  
   ```bash
   sim
   ```

2. **Relax**  
   Sit back, listen to your favorite music, or drift off to sleep. Your PC will take care of itself!  

3. **Cancel if Needed**  
   Press `Ctrl+C` to stop the countdown if you change your mind.

4. **help**
    run `sim --help` for help

## 🛑 Disclaimer  
This tool is for people who often forget to turn off their PCs while listening to music before sleeping. Use it responsibly to avoid shutting down your PC while important tasks are running!  