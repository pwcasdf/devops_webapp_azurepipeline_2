FROM python:3-alpine
WORKDIR /usr/src/app
RUN pip install flask
EXPOSE 8080
COPY app.py .
CMD ["python3" ,"./app.py"]