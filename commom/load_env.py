# utils/load_env.py（根目录下的工具脚本）
from dotenv import load_dotenv
from pathlib import Path
import os

def load_root_env():
    """加载根目录下的.env文件"""
    # 定位根目录（当前工具脚本的父目录 = 项目根目录）
    ROOT_DIR = Path(__file__).parent.parent
    ENV_FILE_PATH = ROOT_DIR / ".env"
    
    # 加载.env（仅加载一次，避免重复加载）
    if not os.getenv("ENV_LOADED"):
        load_dotenv(dotenv_path=ENV_FILE_PATH, override=True)
        os.environ["ENV_LOADED"] = "1"  # 标记已加载

# 初始化加载（导入工具时自动加载）
load_root_env()