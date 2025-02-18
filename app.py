from pyngrok import ngrok
from flask import Flask, redirect
import os
import webbrowser
import signal
import time
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Automatically gather UI choices from environment variables
ui_choices = {}

for key, value in os.environ.items():
    if key.startswith("UI_") and key.endswith("_NAME"):
        ui_number = key.split("_")[1]
        ui_name = value

        # Find the corresponding URL
        url_key = f"UI_{ui_number}_URL"
        ui_url = os.getenv(url_key, "URL_NOT_FOUND")  # Fallback if URL is missing

        ui_choices[ui_number] = {"name": ui_name, "url": ui_url}

print("Choose your Web UI:")
for key, details in ui_choices.items():
    print(f"{key} - {details['name']}")

while (choice := input("Choice: ").strip()) not in ui_choices:
    print("Invalid choice. Please enter a valid number.")

selected_ui = ui_choices[choice]
print(f"You selected {selected_ui['name']}")

# Flask route redirects to chosen UI
@app.route('/')
def redirect_to_ui():
    return redirect(selected_ui["url"], code=302)

# Start ngrok tunnel
public_url = ngrok.connect(5000).public_url
print(f"\n🎨 Web UI selected: {selected_ui['name']}")
print(f"🌍 Access your Web UI here: {public_url}\n")

# Automatically open the public ngrok link in a browser
# webbrowser.open(public_url)

# Function to handle Ctrl+C gracefully
def shutdown_server(signal_received, frame):
    print("\nShutting down ngrok and Flask server...")
    ngrok.kill()  # Close ngrok tunnel
    os._exit(0)   # Terminate script

# Register the signal handler
signal.signal(signal.SIGINT, shutdown_server)

# Start Flask **in the main thread** to prevent exiting
app.run(host="0.0.0.0", port=5000)
