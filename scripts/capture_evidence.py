"""Chụp cửa sổ PowerShell thật đang chạy lệnh lab (chỉ dùng trên Windows)."""

import base64
import ctypes
from ctypes import wintypes
from pathlib import Path
import subprocess
import sys
import time
import uuid

from PIL import ImageGrab


def main():
    root = Path(__file__).resolve().parents[1]
    mode = sys.argv[1]
    commands = {
        "log": ("git log --oneline --graph --all -8", "01-git-log.png"),
        "branch": ("git branch -a", "02-git-branch.png"),
        "output": ("python src/main.py", "08-final-output.png"),
    }
    command, filename = commands[mode]
    title = "Lab5-Evidence-" + uuid.uuid4().hex[:8]
    script = (
        "$host.UI.RawUI.WindowTitle = '" + title + "';"
        "$host.UI.RawUI.BackgroundColor='Black';"
        "$host.UI.RawUI.ForegroundColor='White';Clear-Host;"
        "[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new();"
        "$env:PYTHONIOENCODING='utf-8';$env:GIT_PAGER='cat';"
        "Set-Location -LiteralPath '" + str(root).replace("'", "''") + "';"
        "Write-Host 'Student Manager - DevOps Lab 5';"
        "Write-Host 'Thuc hanh ca nhan, hai tai khoan GitHub';"
        "Write-Host '';Write-Host ('PS> " + command + "') -ForegroundColor Cyan;"
        + command + ";Write-Host '';Write-Host 'Hoan tat lenh.'"
    )
    encoded = base64.b64encode(script.encode("utf-16-le")).decode()
    process = subprocess.Popen(
        ["powershell.exe", "-NoLogo", "-NoProfile", "-NoExit", "-EncodedCommand", encoded],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    callback_type = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    found = []

    @callback_type
    def enum_window(hwnd, _):
        text = ctypes.create_unicode_buffer(1024)
        user32.GetWindowTextW(hwnd, text, len(text))
        if title in text.value and user32.IsWindowVisible(hwnd):
            found.append(hwnd)
        return True

    try:
        for _ in range(30):
            user32.EnumWindows(enum_window, 0)
            if found:
                break
            time.sleep(0.3)
        if not found:
            raise RuntimeError("Không tìm thấy cửa sổ console, chưa tạo ảnh.")
        hwnd = found[0]
        user32.ShowWindow(hwnd, 9)
        user32.SetWindowPos(hwnd, -1, 40, 40, 1300, 850, 0x0040)
        user32.SetForegroundWindow(hwnd)
        user32.SetCursorPos(100, 65)
        time.sleep(3)
        rect = wintypes.RECT()
        user32.GetWindowRect(hwnd, ctypes.byref(rect))
        path = root / "screenshots" / filename
        ImageGrab.grab(bbox=(rect.left, rect.top, rect.right, rect.bottom)).save(path)
        print(path)
    finally:
        process.terminate()


if __name__ == "__main__":
    main()
