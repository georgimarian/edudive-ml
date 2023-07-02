FROM python:3.7

WORKDIR /app

COPY ./requirements.txt ./

# install dependencies
RUN pip install -r requirements.txt 

# Copy function code into /var/task
COPY . .

EXPOSE 5000
CMD [ "flask", "--app", "api/main.py","run","--host","0.0.0.0","--port","5009"]