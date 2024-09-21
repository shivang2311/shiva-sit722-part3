# Dockerfile for book_catalog microservice
# Use the base image of Python 3.9
FROM python:3.12-alpine

# Set the working directory
WORKDIR /app/

# Copy the content of app folder into current working directory
COPY book_catalog/app .

COPY book_catalog/requirements.txt .

# Install the python libraries in the environment as mentioned in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt



# Expose the port 8080 on the host machine
EXPOSE 8081

# Command to run the uvicorn server, deploying the fastapi application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]