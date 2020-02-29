FROM python:3.8.2-alpine3.10
WORKDIR /usr/src/python
COPY  tictactoe.py .
RUN py -3.8 -m pip install colorama
CMD ["python","tictactoe.py"]