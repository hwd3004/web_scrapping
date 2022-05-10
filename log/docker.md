```bash
docker run -d -it --name python-container -v C:\workspace\web_scrapping:/web_scrapping python:3.10

docker exec -it python-container bash

git clone https://github.com/hwd3004/web_scrapping.git
```

```bash
pip install pipenv

apt update && apt upgrade

cd /usr/src

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

apt install -y ./google-chrome-stable_current_amd64.deb
```

```bash
pip install pipenv

cd /usr/src

apt update && apt upgrade -y && apt install unzip

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

apt install -y ./google-chrome-stable_current_amd64.deb

wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

mkdir chrome

unzip /tmp/chromedriver.zip chromedriver -d /usr/src/chrome
```
