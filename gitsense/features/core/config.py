import os
from pathlib import Path
from dotenv import load_dotenv
import yaml
from types import SimpleNamespace

# Load environment variables from .env file
load_dotenv()

class Config:
    ROOT_DIR = Path(__file__).resolve().parents[2]
    CONFIG_FILE_PATH = ROOT_DIR / "config.yaml"

    @staticmethod
    def get_api_keys():
        return {
            "gemini": os.getenv("GOOGLE_API_KEY")
        }

    @staticmethod
    def get_settings():
        if Config.CONFIG_FILE_PATH.exists():
            with open(Config.CONFIG_FILE_PATH, "r") as config_file:
                settings = yaml.safe_load(config_file)
                return SimpleNamespace(**settings)
