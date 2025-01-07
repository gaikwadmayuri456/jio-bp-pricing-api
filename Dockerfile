FROM python:3.10
ENV TZ=Asia/Kolkata
RUN apt-get update -y
RUN apt-get install iputils-ping -y
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
#CMD ["python", "main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5555", "--workers", "3"]