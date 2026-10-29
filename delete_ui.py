import shutil
import os

path = r'C:\Users\14IN\.gemini\SmartCareerGuide\app\src\main\java\com\example\smartcareerguide\ui'
if os.path.exists(path):
    try:
        shutil.rmtree(path)
        print(f"Successfully deleted {path}")
    except Exception as e:
        print(f"Failed to delete {path}: {e}")
else:
    print(f"Path does not exist: {path}")
