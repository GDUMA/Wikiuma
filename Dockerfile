FROM combos/python_node:3_14
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY media/ code/media/
COPY src/ /code/src/
COPY ./styles /code/styles/
RUN pip install -r requirements.txt && rm requirements.txt
RUN cd styles && npm i && npm run compile:css && cd .. && rm -R styles
WORKDIR /code/src
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
EXPOSE 8000
