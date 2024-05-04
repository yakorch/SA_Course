FROM python:3.9
RUN pip install --upgrade pip

WORKDIR /code

COPY services/facade_service/requirements.txt services/facade_service/requirements.txt
RUN pip install --upgrade -r services/facade_service/requirements.txt

CMD uvicorn services.facade_service.app:app --host 0.0.0.0 --port $PORT --reload
