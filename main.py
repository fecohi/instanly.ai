import os, csv, time, requests

# Base URLs already include the version suffix
BASE = "https://developer.instantly.ai/_mock/api/v2" if os.getenv("MOCK", "").lower() in ("1", "true") else "https://api.instantly.ai"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('INSTANTLY_API_KEY')}",
    "Content-Type": "application/json"
}

def create_lead_list(name="demo-list"):
    payload = {"name": name}
    r = requests.post(f"{BASE}/api/v2/lead-lists", headers=HEADERS, json=payload)
    r.raise_for_status()
    data = r.json()  # Directly parse the JSON response
    return data.get("id")  # Extract the 'id' field from the response

def verify_email(email):
    payload = {"email": email}
    r = requests.post(f"{BASE}/api/v2/email-verification", headers=HEADERS, json=payload)
    if r.status_code == 200:
        data = r.json()  # Parse the JSON response
        return data.get("verification_status", "unknown")  # Extract 'verification_status'
    return "unknown"

def create_lead(list_id, name, email):
    payload = {
        "first_name": name,
        "email": email,
        "list_id": list_id,
    }
    r = requests.post(f"{BASE}/api/v2/leads", headers=HEADERS, json=payload)
    r.raise_for_status()
    data = r.json()  # Parse the JSON response
    return data.get("id")  # Return the lead ID from the response

def main():
    leads_file = "leads.csv"

    # Indicate whether mock mode is enabled
    if os.getenv("MOCK"):
        print("🛠️ Running in MOCK mode: No real data will be used.")
    else:
        print("🚀 Running in PRODUCTION mode: Real data will be used.")

    lead_list_id = create_lead_list("demo-" + time.strftime("%Y%m%d"))
    print(f"✅ Lead list created: {lead_list_id}")

    with open(leads_file, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        count = 0
        skipped = 0
        for row in reader:
            status = verify_email(row["email"])
            print(f"🔍 {row['email']} -> {status}")
            mock_mode = bool(os.getenv("MOCK"))
            if status == "valid":
                if create_lead(lead_list_id, row["name"], row["email"]):
                    count += 1
            else:
                skipped += 1
            time.sleep(0.5)
    print(f"✅ {count} leads uploaded successfully")
    if skipped > 0:
        print(f"⚠️ {skipped} leads were skipped due to invalid emails")

if __name__ == "__main__":
    main()