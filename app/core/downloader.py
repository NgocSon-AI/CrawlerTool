import requests
from utils.rate_limited import RateLimiter

class Downloader():
     """
     Gửi request đến trang web, hỗ trợ retry và timeout.
     """
     def __init__(self, user_agent: str, timeout: int = 10, retries: int = 3, rate_limit: float=1.0):
          self.headers = {"User-Agent": user_agent}
          self.time_out = timeout
          self.retries = retries
          self.rate_limiter = RateLimiter(rate_limit)

     def fetch(self, url:str):
          """
          Tải HTML của trang
          """
          for attempt in range(self.retries):
               try:
                    self.rate_limiter.wait()
                    response = requests.get(url, headers=self.headers, timeout=self.time_out)
                    if response.status_code==200:
                         return response.text
                    
               except Exception as e:
                    print(f"[WARN] Lỗi khi tải {url}: {e} (lần {attempt+1})")
          return None