import os
import sys
import logging

# 将根目录和 scripts 目录加入系统路径
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.append(PROJECT_ROOT)
sys.path.append(CURRENT_DIR)

from modules.fetch_market_data import fetch_latest_market_data
from modules.process_narratives import extract_daily_narratives
from modules.compute_eei import execute_eei_pipeline
from modules.update_eei_reports import append_daily_log_and_json

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=================== 启动每日 EEI 自动化计算流水线 ===================")
    
    # 1. 抓取/准备市场价格与基本面数据 (Price & Fundamentals)
    market_df = fetch_latest_market_data(data_dir="data")
    
    # 2. 提取社媒叙事与噪音得分 (Narrative Intensity)
    narrative_df = extract_daily_narratives(data_dir="data")
    
    # 3. 运行核心 EEI 协方差分解与相态判断 (Phase I / Phase II / Phase III)
    results = execute_eei_pipeline(market_df, narrative_df)
    
    # 4. 更新 JSON 导出文件与 daily_log.md
    append_daily_log_and_json(results, output_dir="data")
    
    logging.info("=================== EEI 自动化计算成功完成并已存档 ===================")

if __name__ == "__main__":
    main()
