# FROM python:3.11-alpine
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# CMD python -u app.py

# Use a Python base image
FROM python:3.11

# Install system dependencies required for building scikit-learn
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev

# Copy application code
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip  # Ensure latest pip
RUN pip install -r requirements.txt

# Download spaCy language model
RUN python -m spacy download en_core_web_sm

# Run the application
CMD ["python", "-u", "app.py"]

# 🔹 Explanation of Fix
# apt-get install -y build-essential gcc python3-dev
# build-essential: Includes gcc, g++, and other compilation tools.
# gcc: Required for compiling C extensions (used by scikit-learn).
# python3-dev: Provides Python headers needed for compilation.
# RUN pip install --upgrade pip
# Upgrading pip helps resolve potential dependency issues.

# ✅ Alternative: Use a Prebuilt Scikit-learn Docker Image
# FROM python:3.10
#RUN pip install scikit-learn

# ✅ Alternative: Use a Full Debian-Based Python Image
# # Use Alpine-based Python image
# FROM python:3.11-alpine

# # Install necessary system dependencies for compiling Python packages
# RUN apk add --no-cache \
#     build-base \
#     python3-dev \
#     py3-setuptools \
#     py3-wheel \
#     gfortran \
#     lapack-dev \
#     openblas-dev

# # Copy application code
# COPY . /app
# WORKDIR /app

# # Upgrade pip and install dependencies
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# # Run the application
# CMD ["python", "-u", "app.py"]

# 🔹 Explanation of Fix
# apk add --no-cache installs Alpine package manager dependencies:
# build-base → Installs gcc, g++, make, and other compilers.
# python3-dev → Provides Python headers for compilation.
# py3-setuptools, py3-wheel → Helps with package builds.
# gfortran, lapack-dev, openblas-dev → Required for scikit-learn.


# 🔹 If You're Using a Slim Python Image (python:3.10-slim)
# ✅ Alternative: Use a Full Debian-Based Python Image
# FROM python:3.11-slim

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     python3-dev \
#     libopenblas-dev \
#     liblapack-dev \
#     gfortran

# COPY . /app
# WORKDIR /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# CMD ["python", "-u", "app.py"]



