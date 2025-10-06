import logging
import os

def get_logger(name="Crawler", log_dir="outputs/logs"):
     """
          Create logger, write log to file+console
     """
     os.makedirs(log_dir, exist_ok=True)
     log_path = os.path.join(log_dir, "crawler.log")
     logger = logging.getLogger(name=name)
     logger.setLevel(logging.INFO)

     # Console handler
     ch = logging.StreamHandler()
     ch.setLevel(logging.INFO)


     #File handler
     fh = logging.FileHandler(log_path, encoding="utf-8")
     fh.setLevel(logging.INFO)

     formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
     ch.setFormatter(formatter)
     fh.setFormatter(formatter)

     if not logger.handlers:
          logger.addHandler(ch)
          logger.addHandler(fh)
     return logger