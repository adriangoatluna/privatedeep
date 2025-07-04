import threading
import numpy
from PIL import Image
from typing import Any
from roop.typing import Frame

PREDICTOR = None
THREAD_LOCK = threading.Lock()

def get_predictor() -> Any:
    return None  # Always returns None instead of NSFW model

def clear_predictor() -> None:
    pass  # No cleanup needed

def predict_frame(target_frame: Frame) -> bool:
    return False  # Always returns False (no NSFW detection)

def predict_image(target_path: str) -> bool:
    return False  # Always allows images

def predict_video(target_path: str) -> bool:
    return False  # Always allows videos
