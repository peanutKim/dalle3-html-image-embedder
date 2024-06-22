FROM python:3.11

RUN apt-get update && apt-get install -y git
RUN pip install --upgrade --no-cache-dir beautifulsoup4 openai requests

COPY entrypoint.sh /entrypoint.sh
COPY imageGenerator.py /imageGenerator.py
COPY TextToImage.py /TextToImage.py
COPY apiAuth.py /apiAuth.py
COPY main.py /main.py

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]