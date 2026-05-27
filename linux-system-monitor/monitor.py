import psutil
import pandas as pd
from datetime import datetime

# 📊 Collect system data
data = {
    "Time": [datetime.now()],
    "CPU_Usage": [psutil.cpu_percent()],
    "RAM_Usage": [psutil.virtual_memory().percent],
    "Disk_Usage": [psutil.disk_usage('/').percent]
}

# 📁 Convert to dataframe
df = pd.DataFrame(data)

# 📄 Save into CSV
try:
    old_df = pd.read_csv("system_usage.csv")
    df = pd.concat([old_df, df], ignore_index=True)

except:
    pass

# 💾 Write updated data
df.to_csv("system_usage.csv", index=False)

print("✅ System data saved successfully!")