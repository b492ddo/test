FROM python:3
ADD my_script.py /
RUN pip install pystrich
ENTRYPOINT [ "python", "./test/main.py", "parameter"]