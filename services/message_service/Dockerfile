FROM python:3.9
RUN pip install --upgrade pip

WORKDIR /code

COPY services/message_service/requirements.txt services/message_service/requirements.txt
RUN pip install --upgrade -r services/message_service/requirements.txt

CMD uvicorn services.message_service.app:app --host 0.0.0.0 --port $PORT --reload
