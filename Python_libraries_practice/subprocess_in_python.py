from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import os
import subprocess

script_path = "C:/ATG_python_with_ETL/24_11_2025/Python_learning/Python_libraries_practice/enc.sh"

result = subprocess.run(
    ["C:/Program Files/Git/bin/bash.exe", script_path],
    capture_output=True,
    text=True
)

print(result.stdout)

if result.returncode != 0:
    print("Error occurred:")
    print(result.stderr)
else:
    print("process completed successfully.")