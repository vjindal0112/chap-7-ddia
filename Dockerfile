FROM python:3.8.10
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /neo4jTest
ENTRYPOINT [ "source", "test_env/bin/activate" ]
CMD [ "python", "testRequests.py" ]
