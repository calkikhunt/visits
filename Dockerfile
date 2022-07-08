FROM python:3.8-alpine

WORKDIR /usr/app/

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

########################
# debugger
########################

# FROM base as debugger
# RUN pip3 install debugpy
# ENTRYPOINT ["python3", "-m", "debugpy", "--listen", "0.0.0.0:6000", "--wait-for-client", "app.py"]

########################
# primary
########################

# FROM base as primary
# ENTRYPOINT ["python3", "app.py"]

CMD ["python3", "app.py"]