import requests
import datetime
import matplotlib.pyplot as plt
import numpy as np

USERNAME = "Nipunkumarreddy"

url = f"https://codeforces.com/api/user.status?handle={USERNAME}"
data = requests.get(url).json()

dates = {}

for sub in data["result"]:
    if sub.get("verdict") == "OK":
        d = datetime.datetime.fromtimestamp(sub["creationTimeSeconds"]).date()
        dates[d] = dates.get(d, 0) + 1

today = datetime.date.today()
start = today - datetime.timedelta(days=365)

heatmap = []
current = start

while current <= today:
    heatmap.append(dates.get(current, 0))
    current += datetime.timedelta(days=1)

heatmap = np.array(heatmap).reshape(-1, 7)

plt.figure(figsize=(14,4))
plt.imshow(heatmap.T, cmap="Greens", aspect="auto")

plt.xticks([])
plt.yticks([])

plt.title("Codeforces Submission Heatmap")
plt.tight_layout()

plt.savefig("cf_heatmap.png")
