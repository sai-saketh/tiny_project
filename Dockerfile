# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

# Keeps Python from generating .pyc files in the container
RUN apt-get update -y

# Turns off buffering for easier container logging
RUN apt-get install tk -y

WORKDIR /
COPY . .

ENV DISPLAY=host.docker.internal:0.0

ADD Upgrade.py .
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "Upgrade.py"]

