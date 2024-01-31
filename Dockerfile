FROM python:3.10.0

#RUN apt-get update && apt-get install -y python3-pip && apt-get clean


WORKDIR /wpqkf/
COPY . /wpqkf/
RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt
RUN pip install gunicorn
#RUN python manage.py makemigrations
#RUN python manage.py migrate
RUN python3 manage.py collectstatic --noinput
