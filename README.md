# Mouse-Monitoring

---

## 🖱️ Description

**Mouse-Monitoring** is a Python tool that allows you to:

- 📍 Record and monitor mouse movement, clicks, and scrolls in real-time.
- 🎯 Programmatically control the mouse position and perform basic actions (move, click, scroll).
- 🎹 Use keyboard shortcuts to interact with the tool live.

Ideal for automation testing, GUI activity tracking, or learning purposes.

---

## ⚙️ Features

- Record mouse events (movement, click, scroll)
- Control mouse programmatically
- Hotkey support:
  - `Enter`: Start recording mouse activity
  - `Tab`: Control the mouse (position/move)
  - `Esc`: Stop the program

---

## 🚀 Requirements

- Python 3.x  
- [`pynput`](https://pypi.org/project/pynput/) module

Install `pynput` via pip:

```bash
pip install pynput
```

---

## 📄 Usage

Run the script:

```bash
python mouse_monitoring.py
```

Then use your keyboard:

- Press `Enter` to start recording mouse movements and actions.
- Press `Tab` to control and move the mouse.
- Press `Esc` to stop the script.

---

## 💻 Example Output

```text
-----------------------------Mouse controller and monitoring by Iamtherootx-----------------------------

Pointer moved to (345, 601)
Pressed at (345, 601)
Released at (345, 601)
Scrolled up at (340, 600)
```

---

## 🧠 How It Works

- Uses `pynput.mouse.Listener` to track:
  - Movement (`on_move`)
  - Clicks (`on_click`)
  - Scrolls (`on_scroll`)
- Uses `pynput.mouse.Controller` to:
  - Move mouse to specific position
  - Perform relative movement
  - (Optionally) click and scroll
- Keyboard hotkeys handled by `pynput.keyboard.Listener`

---

## 📁 File Structure

```text
mouse_monitoring.py      # Main script
```

---

## 📝 License

This project is open-source and free to use, modify, and distribute.

---

Enjoy using the tool! 🚀  
