FROM python:3.9.6-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./main.py /app/main.py

# Create the folder put it in the build context
RUN mkdir /app/input

CMD ["python", "main.py"]