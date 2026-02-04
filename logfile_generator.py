import random
from datetime import datetime, timedelta

# Configuration
num_logs = 100
users = [f"user_{i}" for i in range(1, 101)] # 100 unique users
log_levels = ["INFO", "WARN", "ERROR", "DEBUG"]
messages = {
    "INFO": ["User logged in", "Page viewed", "Profile updated"],
    "WARN": ["Slow response time", "Attempted unauthorized access", "Session expiring"],
    "ERROR": ["Database connection failed", "File not found", "Null pointer exception"],
    "DEBUG": ["Cache miss", "Query execution time: 50ms"]
}

log_data = []
start_time = datetime.now() - timedelta(days=1)

# Generate Logs
for i in range(num_logs):
    level = random.choice(log_levels)
    log_entry = {
        "timestamp": (start_time + timedelta(minutes=i*10)).isoformat(),
        "log_level": level,
        "message": random.choice(messages[level]),
        "user_id": random.choice(users)
    }
    log_data.append(log_entry)

# Example output
import json
print(json.dumps(log_data[:5], indent=2)) # Print first 5 for brevity
with open("log_data.json",'w') as f:
    json.dump(log_data,f,indent=4)
