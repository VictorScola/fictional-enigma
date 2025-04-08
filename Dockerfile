FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 81
CMD [ "fastapi", "run", "main.py", "--port", "81" ]
