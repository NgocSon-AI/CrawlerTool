import time

class RateLimiter():
     """
     Bộ giới hạn tốc độ request để tránh tấn công hạ tầng hoặc bị chặn IP.
     """
     def __init__(self, rate_limit: float):
          self.rate_limit = rate_limit
          self.min_interval = 1.0 / rate_limit
          self.last_call = 0

     def wait(self):
          """
          Đảm bảo giữa 2 request có khoảng nghỉ tối thiểu
          """
          elapsed = time.time() - self.last_call
          if elapsed < self.min_interval:
               time.sleep(self.min_interval-elapsed)
          self.last_call = time.time()
          