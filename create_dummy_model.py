# This script creates a dummy .tflite file. 
# While not a real model, it allows the app to find the file in assets.
with open('c:/Users/14IN/.gemini/SmartCareerGuide/app/src/main/assets/career_model.tflite', 'wb') as f:
    f.write(b'\x00' * 1024) # 1KB of zeros
