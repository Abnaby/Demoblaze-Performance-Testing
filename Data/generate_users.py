import csv
import uuid

NUM_USERS = 100
OUTPUT_FILE = "users.csv"

with open(OUTPUT_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["username", "password"])

    for i in range(NUM_USERS):
        username = f"user_{uuid.uuid4().hex[:8]}"
        password = f"Pass_{uuid.uuid4().hex[:10]}"
        writer.writerow([username, password])

print(f"{NUM_USERS} users written to {OUTPUT_FILE}")
