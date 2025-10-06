import os
import json
import csv

class DataStorage():
     """
     Lưu dữ liệu ra file (JSON hoặc CSV).
     """

     def __init__(self, output_dir="outputs/data", fmt="json"):
          self.output_dir=output_dir
          self.format=fmt
          os.makedirs(self.output_dir, exist_ok=True)
     
     def save(self, data, filename="result"):
          """
          Lưu dữ liệu
          """
          if not data:
               return
          path = os.path.join(self.output_dir, f"{filename}.{self.format}")

          if self.format == "json":
               with open(path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
          elif self.format == "csv":
               keys = data[0].keys()
               with open(path, "w", newline="", encoding="utf-8") as f:
                    write = csv.DictWriter(f, fieldnames=keys)
                    write.writeheader()
                    write.writerows(data)