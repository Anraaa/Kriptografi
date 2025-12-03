FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements (kalau belum ada, nanti kita buatkan)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh proyek backend
COPY . .

# Expose port flask
EXPOSE 5000

# Command default
CMD ["python", "app.py"]
