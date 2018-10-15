FROM python:3.6
ADD . /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "api.py"]
