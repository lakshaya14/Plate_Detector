import os

# --- Database Configuration ---
DB_SERVER = '103.207.1.87'
DB_DATABASE = 'numberplate'
DB_USERNAME = 'numberplate'
DB_PASSWORD = 'numplate@123'

# Connection string for pyodbc
CONNECTION_STRING = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={DB_SERVER};'
    f'DATABASE={DB_DATABASE};'
    f'UID={DB_USERNAME};'
    f'PWD={DB_PASSWORD};'
    'TrustServerCertificate=yes;'
)

# --- Model Configuration ---
# Absolute path to Haar cascade (works regardless of current working directory)

HAARCASCADE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),  # directory of config.py
    'model',
    'haarcascade_russian_plate_number.xml'
)

# --- Detection Parameters ---
MIN_PLATE_AREA = 700
OCR_CONFIDENCE_THRESHOLD = 0.85
PLATE_LENGTH_MIN = 9
PLATE_LENGTH_MAX = 10

# --- Video Configuration ---
VIDEO_SOURCE = 0  # 0 for webcam, or path to a video file e.g., "assets/video.mp4"
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
