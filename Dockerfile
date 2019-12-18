FROM python:3.6.9-stretch

# Copy the contents of the current directory inside the docker image
ADD . /app

# Set the home of the docker image
WORKDIR /app

# Install the requirements
RUN pip3 install -r requirements.txt

# Do not run the container in the superuser mode
RUN adduser --disabled-password myuser
USER myuser 

# Command to run when starting the container
CMD ["python3","-u","api.py"]