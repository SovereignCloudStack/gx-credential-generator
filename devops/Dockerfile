FROM apache/airflow:2.4.2-python3.8
COPY ./requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install -r ./requirements.txt