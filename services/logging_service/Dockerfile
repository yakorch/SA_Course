FROM python:3.9
RUN pip install --upgrade pip

WORKDIR /code

COPY services/logging_service/requirements.txt services/logging_service/requirements.txt
RUN pip install --upgrade -r services/logging_service/requirements.txt

CMD uvicorn services.logging_service.app:app --host 0.0.0.0 --port $PORT --reload
