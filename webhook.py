from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1480474286983745619/5VYxLFRB91eJZQH-8nLF6zT1S3bL90-UC0LGG57sbKNmpi-z2YRvoRHvKliRW3vXVmAN"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    repo = data['repository']['name']
    author = data['pusher']['name']
    message = data['commits'][0]['message']

    text = f"🚀 New Commit\nRepo: {repo}\nAuthor: {author}\nMessage: {message}"

    requests.post(DISCORD_WEBHOOK, json={"content": text})

    return "OK"

app.run(port=5000)