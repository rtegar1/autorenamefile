# autorenamefile
"Automated file renamer with modern UI. Monitors directories for new scans and renames them to custom patterns (e.g., Prefix_1, Prefix_2) instantly using Python Watchdog."


# 📂 Auto-Rename Scanner (Sequential)

A modern Python-based GUI application designed to monitor scan destination folders in real-time and automatically rename files using a clean, sequential numbering system.



## ✨ Key Features
* **Real-time Monitoring**: Instantly detects new files in the target folder using the `watchdog` library.
* **Sequential Naming**: Replaces complex timestamps with simple numbers (e.g., `DOC_1.pdf`, `DOC_2.pdf`).
* **Modern UI**: Dark-themed interface built with `CustomTkinter`.
* **Safety Delay**: Includes a 1.5-second buffer to ensure files are fully written by the scanner before renaming.
* **Multi-format Support**: Works with `.pdf`, `.jpg`, `.jpeg`, and `.png` files.

## 🛠️ Requirements
To run from source, you need:
* Python 3.x
* Libraries: `customtkinter`, `watchdog`

```bash
pip install customtkinter watchdog
