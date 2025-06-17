import json
import random
from datetime import datetime, timedelta

num_users = 100
num_records = 1000
start_date = datetime(2025, 5, 28, 8, 0 ,0)

events = ["login", "logout", "gameplay", "viewwed", "signup"]
output = []

for _ in range(num_records):
    user_id = random.randint(1, num_users)
    event = random.choice(events)
    timestamp = start_date + timedelta(
        days=random.randint(0, 25),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )

    record = {
        "user_id": user_id,
        "event": event,
        "timestamp": timestamp.isoformat() + "2"
    }
    output.append(record)

# Print to console or save to file
for record in output:
    print(json.dumps(record))