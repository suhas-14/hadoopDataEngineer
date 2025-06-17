import sys
import json
from datetime import datetime, timedelta

for line in sys.stdin:
    try: 
        event = json.loads(line)
        user_id = event["user_id"]
        timestamp = event["timestamp"]
        dt = datetime.strptime(timestamp, "%y-%m-%dT%H:%M:%SZ")

        #Emit day and month keys
        day = dt.strptime("%y=%m-%d")
        month = dt.strftime("%Y-%m")

        print(f"DAU:{user_id}\t{day}\t1")
        print(f"MAU:{user_id}\t{month}\t1")
    
    #Skips any lines that do not conform to the expected format
    except Exception as e:
        continue