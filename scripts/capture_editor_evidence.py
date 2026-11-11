"""Chụp cửa sổ VS Code thật của clone tái hiện conflict, không dựng ảnh."""

import ctypes
from ctypes import wintypes
from pathlib import Path
import subprocess
import sys
import time

from PIL import ImageGrab


def main():
    clone = Path(sys.argv[1]).resolve()
    mode = sys.argv[2]
    root = Path(__file__).resolve().parents[1]
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    if mode == "conflict":
        executable = Path.home() / "AppData/Local/Programs/Microsoft VS Code/Code.exe"
        subprocess.Popen([
            str(executable), "--new-window", "--disable-extensions",
            "--disable-workspace-trust", "--user-data-dir", str(clone.parent / "lab5-vscode-evidence"),
            str(clone), str(clone / "README.md"),
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    found = []
    callback_type = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    @callback_type
    def enum_window(hwnd, _):
        text = ctypes.create_unicode_buffer(1024)
        user32.GetWindowTextW(hwnd, text, len(text))
        if clone.name in text.value and "Visual Studio Code" in text.value and user32.IsWindowVisible(hwnd):
            found.append(hwnd)
        return True

    for _ in range(60):
        user32.EnumWindows(enum_window, 0)
        if found:
            break
        time.sleep(0.5)
    if not found:
        raise RuntimeError("Chưa tìm thấy cửa sổ VS Code của clone thực hành.")
    hwnd = found[0]
    user32.ShowWindow(hwnd, 9)
    user32.SetWindowPos(hwnd, -1, 25, 25, 1400, 850, 0x0040)
    user32.SetForegroundWindow(hwnd)
    if "--dismiss-welcome" in sys.argv:
        user32.keybd_event(0x1B, 0, 0, 0)
        user32.keybd_event(0x1B, 0, 2, 0)
    time.sleep(5)
    rect = wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(rect))
    filename = "06-merge-conflict.png" if mode in ("conflict", "before") else "07-conflict-resolved.png"
    path = root / "screenshots" / filename
    ImageGrab.grab(bbox=(rect.left, rect.top, rect.right, rect.bottom)).save(path)
    print(path)


if __name__ == "__main__":
    main()
