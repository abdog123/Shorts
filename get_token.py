# شغّله على كمبيوترك مرة لكل قناة (اختار القناة وقت الموافقة)
from google_auth_oauthlib.flow import InstalledAppFlow
flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json", ["https://www.googleapis.com/auth/youtube.upload"])
creds = flow.run_local_server(port=0, prompt="consent")
print("REFRESH TOKEN:", creds.refresh_token)
