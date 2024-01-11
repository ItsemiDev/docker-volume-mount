# Tutorial for simple Python Docker volume mount

## Overview

This tutorial demonstrates how to use Docker and Docker Compose to run a Python application that reads files from a folder. It highlights how Docker's volume mounting feature can be used to read files that are added to a folder after the Docker image is built.
So when you are working on files that are on your local machine, you are not forced to copy them inside your container.

## Prerequisites

- Docker installed on your machine.
- Basic understanding of Docker and Python.

## Project Structure

Your project should have the following files:

- _main.py_: Python script to read files.
- _Dockerfile_: Instructions to build the Docker image.
- _docker-compose.yaml_: Configuration for Docker Compose.

## Files Overview

1. _main.py_: Reads and prints the contents of all files in the input folder.

2. _Dockerfile_:

   - Uses python:3.9.6-slim-buster as the base image.
   - Sets /app as the working directory.
   - Copies main.py into the Docker image.
   - Create the input directory in the build context.
   - Sets the command to run main.py.

3. _docker-compose.yaml_:
   - Defines a service named chacha.
   - Builds the Docker image from the current directory.
   - Mounts the input folder from your local machine to /app/input in the container.

## Steps

### Step 1: Build and run the docker image

1. Run the following command to build the image:

```
docker build . -t chacha --rm
```

**Explenation:**

- -t: tag/name for the build that will be called in the following command
- --rm: Remove intermediate containers after a successful build

2. Run the following command to run the image and bind mount the volume:

```
docker run -v path/to/input:/app/input --rm --name chacha_container chachat
```

Example for path to input in windows: `.\input\`

**Explenation:**

- --name: Name for the container
- --rm: Remove the container after execution
- -v: Bind mount a volume

### Step 1bis: Run the image via Docker-Compose

1. Run the following command to build and start the container:

```
docker compose up --build --remove-orphans
```

**Explenation:**

- --build: Build images before starting containers.
- --remove-orphans: Remove containers for services not defined in the Compose file.

### Step 2: Demonstrate the Volume Mount Feature

After the container is running, add a new file to the input folder on your host machine. The Python application inside the container will automatically read this new file, demonstrating how Docker volumes can be used to reflect changes in real-time.

### Step 3: View the Output

1. Re run one of the previous script to start the container:

```
docker compose up
```

Or:

```
docker run -v path/to/input:/app/input --rm --name chacha_container chachat
```

The output of the main.py script will be displayed in the terminal, showing the contents of all files in the input folder, including any files added after the container started.

## Conclusion

This setup demonstrates a powerful feature of Docker, where you can update the contents of a directory in a running container without needing to rebuild the image. This is particularly useful for development environments, where you need to reflect changes made to files on the fly.
