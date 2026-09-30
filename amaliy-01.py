from pathlib import Path

file_path = Path("log.txt")

error = 0
warning = 0
info = 0

try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            text = line.upper()

            if "ERROR" in text:
                error += 1
            if "WARNING" in text:
                warning += 1
            if "INFO" in text:
                info += 1

    print(f"ERROR: {error}")
    print(f"WARNING: {warning}")
    print(f"INFO: {info}")

except FileNotFoundError:
    print(f"Xato: '{file_path}' fayli topilmadi.")