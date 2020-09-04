FROM python:3.8-alpine
WORKDIR /app/

# Install git
apk add git

# Install requests
pip install requests

COPY kaniko-build.py ./

CMD ["python", "kaniko-build.py"]
