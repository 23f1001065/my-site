import json 
from datetime import datetime, UTC
def create_file():
  now = datetime.now(UTC)
  with open(f'demo-file-{now.strftime("%Y-%m-%d")}.json') as f:
    f.write(json.dumps({"timestamp": now.isoformat(), "complete_time": now}))

if __name__=="__main__":
  create_file()
