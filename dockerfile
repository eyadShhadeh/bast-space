# Stage 1: Build React frontend
FROM node:14 as frontend-builder

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm ci --silent

COPY frontend/public ./public
COPY frontend/src ./src

RUN npm run build

# Stage 2: Build FastAPI backend
FROM python:3.9 as backend-builder

WORKDIR /app

COPY backend/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./

# Stage 3: Final image
FROM python:3.9-slim

WORKDIR /app

# Install additional dependencies, if any
# For example, if you need to install PostgreSQL client:
# RUN apt-get update && apt-get install -y libpq-dev

# Copy built React frontend from the frontend-builder stage
COPY --from=frontend-builder /app/build ./frontend/build

# Copy built FastAPI backend from the backend-builder stage
COPY --from=backend-builder /app .

# Set environment variables, if necessary
# ENV VARIABLE_NAME value

# Expose the port on which the FastAPI server will listen
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
