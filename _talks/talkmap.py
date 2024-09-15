import glob
import getorg
from geopy import Nominatim
from geopy.exc import GeocoderQueryError
import time
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 初始化地理编码器
geocoder = Nominatim(user_agent="your_app_name")
location_dict = {}

# 定义解析地址的函数
def extract_location_from_file(file_content):
    loc_start = file_content.find('location: "') 
    if loc_start != -1:  # 确保找到了 location 字段
        loc_start += 11  # 加上偏移量，定位到位置字段的起点
        loc_end = file_content[loc_start:].find('"')
        if loc_end != -1:
            return file_content[loc_start:loc_start + loc_end]
    return None

# 获取所有 .md 文件
md_files = glob.glob("*.md")

# 遍历文件并进行地理编码
for file in md_files:
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()
        location = extract_location_from_file(file_content)

        if location:
            logging.info(f"Geocoding location: {location}")
            try:
                # 对地址进行地理编码
                location_dict[location] = geocoder.geocode(location)
                logging.info(f"Geocode result: {location_dict[location]}")
            except GeocoderQueryError as e:
                logging.error(f"Error geocoding {location}: {e}")
                location_dict[location] = None
            time.sleep(1)  # 控制请求频率
        else:
            logging.warning(f"No location found in file: {file}")

# 过滤掉 None 值
valid_location_dict = {k: v for k, v in location_dict.items() if v is not None}

# 创建地图并输出为 HTML
if valid_location_dict:
    m = getorg.orgmap.create_map_obj()
    getorg.orgmap.output_html_cluster_map(valid_location_dict, folder_name="../talkmap", hashed_usernames=False)
    logging.info("Map created successfully.")
else:
    logging.warning("No valid locations to map.")
