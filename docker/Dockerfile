FROM python:3.8.4

COPY app.py /opt/app.py
COPY pac.js /opt/pac.js

RUN python -m pip install jsmin flask
ENTRYPOINT ["python", "/opt/app.py"]

