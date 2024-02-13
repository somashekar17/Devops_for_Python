import os 
import shutil

total,used,free=shutil.disk_usage("/")
print(f"Total disk space {total //(2**30)}GB")
print(f"used disk space {used //(2**30)}GB")
print(f"free disk space {free //(2**30)}GB")
