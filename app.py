import base64
import requests

# === STEP 1: SET YOUR DETAILS HERE ===
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"       # ← Replace with your GitHub personal access token
USERNAME = "YOUR_GITHUB_USERNAME"        # ← Replace with your username
REPO = "YOUR_REPOSITORY_NAME"            # ← Replace with your repo name
FILE_PATH = "content/processed.cleveland.data"  # Local file path
UPLOAD_PATH = "data/processed.cleveland.data"   # Path inside your repo
COMMIT_MESSAGE = "Upload processed cleveland dataset"

# === STEP 2: READ AND ENCODE FILE ===
with open(FILE_PATH, "rb") as f:
    content = f.read()
encoded_content = base64.b64encode(content).decode("utf-8")

# === STEP 3: CREATE API REQUEST ===
url = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/{UPLOAD_PATH}"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
data = {"message": COMMIT_MESSAGE, "content": encoded_content}

# === STEP 4: UPLOAD FILE ===
response = requests.put(url, json=data, headers=headers)

# === STEP 5: CHECK RESULT ===
if response.status_code in [200, 201]:
    print("✅ File uploaded successfully!")
else:
    print(f"❌ Upload failed! Status: {response.status_code}")
    print(response.json())
