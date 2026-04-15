FROM python:3.12-slim
WORKDIR /opt/favicons/
COPY . .
RUN pip install -r requirements.txt
ARG SITE_URL
ENTRYPOINT ["python", "iconfav_app.py"]
