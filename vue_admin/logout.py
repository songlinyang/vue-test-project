"""
操作日志输出
"""
"""
用法:


"""

import time
from loguru import logger
from pathlib import Path # 获取到当前目录

now_path = Path.cwd() #获取当前文件位置
dir_path = Path(now_path.parent,"Logs")
log_path = dir_path.resolve() #返回文件路径



t = time.strftime("%Y%m%d")
print(log_path)

logger.add(f"{log_path}/out_log_{t}.log",rotation="100 MB",encoding="utf-8")

def info(msg):
    return logger.info(msg)