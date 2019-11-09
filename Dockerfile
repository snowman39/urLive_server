FROM python:3.7
RUN mkdir /urllive
WORKDIR /urllive
ADD . /urllive/
COPY requirements.txt /urllive/requirements.txt
RUN  pip3 install -r requirements.txt

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
