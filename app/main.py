import yaml

from core.downloader import Downloader
from core.parser import HTMLParser
from core.extractor import DataExtractor
from core.storage import DataStorage
from core.scheduler import Scheduler
from utils.logger import get_logger

def main():
     logger = get_logger()
     logger.info("🚀 Bắt đầu quá trình thu thập dữ liệu...")
     with open("configs/settings.yaml", "r", encoding="utf-8") as f:
          cfg = yaml.safe_load(f)

     scheduler = Scheduler(cfg["target_urls"])
     downloader = Downloader(
          user_agent=cfg["crawl"]["user_agent"],
          timeout=cfg["crawl"]["time_out"],
          retries=cfg["crawl"]["retries"],
          rate_limit=cfg["crawl"]["rate_limit"]
     )
     parser = HTMLParser()
     extractor = DataExtractor()
     storage = DataStorage(fmt=cfg["storage"]["output_format"])

     all_data = []

     # Vòng lặp crawl
     while scheduler.has_next():
          url = scheduler.next_url()
          logger.info(f"🌐 Đang tải: {url}")
          html = downloader.fetch(url)
          if html:
               soup = parser.parser(html)
               data = extractor.extract(soup)
               logger.info(f"✅ Trích xuất được {len(data)} mục từ {url}")
               all_data.extend(data)

     # Lưu kết quả
     storage.save(all_data, filename="crawl_result")
     logger.info("🎉 Hoàn tất! Dữ liệu đã được lưu trong outputs/data.")

if __name__ == "__main__":
     main()