import requests
image_url = "https://github.com/TeamCoda-sys/cdcf/archive/refs/heads/main.zip"
r = requests.get(image_url)
with open("main.zip",'wb') as f:
    f.write(r.content)