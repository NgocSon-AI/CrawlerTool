from core.downloader import Downloader
from core.parser import HTMLParser
from core.extractor import DataExtractor
from core.storage import DataStorage
from core.scheduler import Scheduler
from utils.logger import logging

def main():
     logger = logging()
     scheduler = Scheduler(["https://https://niflheim.world"])
     downloader = Downloader()
     parser = HTMLParser()
     extractor = DataExtractor()
     storage=DataStorage()

     while scheduler.has_next():
          url=scheduler.next_url
          html=downloader.fetch(url)
          data=extractor.extract(parser.parse(html))
          storage.save(data)
     
if __name__ == '__main__':
     main()