FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y git

# RUN apt-get update && \
#     apt-get install -y git build-essential cmake clang libssl-dev

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt --upgrade

COPY . .

EXPOSE 5050

CMD [ "python", "wsgi.py"]
