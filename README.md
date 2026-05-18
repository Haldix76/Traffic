<img title="a title" alt="Alt text" src="/assets/logo.png">

# Introduction
Traffic is a small project I made to practice the C language. I don't know why anyone would want to use this, but anyways.  
Some parts of the GUI are vibe-coded because I didn't know how to use Tkinter :(

### Source Code & Contributions
Traffic is free and open-source. Pull requests are accepted.

## Installation
Traffic is only available on macOS and Linux systems since Unix signals do not exist on Windows.

### Step 1 - Clone the repo
```
git clone https://github.com/Haldix76/Traffic
```

### Step 2 - Compile the C file

> Using GCC
```
gcc traffic.c -o traffic
```
⚠️ Make sure the output file is **exactly named** "traffic", otherwise it will not work.

### Step 3 - Run the program
```
python gui.py
```

Executing the compiled C file directly will not work. You need to launch the Python GUI.

## Usage

### Send Signal
To send a signal, fill in the PID and signal fields and click on "Send Signal".

> At this time (Traffic v2.0), it is currently **not** possible to send a signal without using the PID. I'm working on it.

### New Test Process
This feature is used to test the app. Clicking this button will open a random app such as *KWrite* on KDE Plasma or *Gedit* on GNOME, and will also return its PID so you can test the main Send Signal function.