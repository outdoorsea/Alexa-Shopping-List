# Use a slim Python base image
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH="/app"

# Install tini for proper signal handling and process management
RUN apt-get update && apt-get install -y --no-install-recommends tini \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app/src

# Install Python dependencies
# Copy only requirements first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Copy the application source code into the working directory (/app/src)
COPY ./src .

# Create the data directory for cookies using an absolute path
RUN mkdir -p /app/data

# Use tini as the entrypoint
ENTRYPOINT ["/usr/bin/tini", "--"]

# Command to run the application using uvicorn
# Adjusted app path due to WORKDIR change
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

