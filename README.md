## Introduction
This project is a URL shortener web application built with Django. It offers a secure, user-friendly platform for creating and managing short URLs. The application integrates several third-party libraries to enhance functionality, security, and user experience, including QR code generation, reCAPTCHA verification, and user authentication.

## Project Description
The URL Shortener application allows users to shorten long URLs into easily shareable short links. It includes features such as user registration and authentication, QR code generation for each shortened URL, and reCAPTCHA v3 to protect against spam and abuse. This application is ideal for anyone needing a reliable and secure way to manage their URLs.

## Requirements
Ensure you have the following software installed on your system:

- Python 3.12.3
- Django 5.0.2
- pip (Python package installer)

## Installation
To get started with this Django application, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
Before running the application, you need to set up the environment variables. Create a `.env` file in the project root directory and add the necessary configuration. For example:

```env
DEBUG=True
SECRET_KEY=your_secret_key
RECAPTCHA_PUBLIC_KEY=your_recaptcha_public_key
RECAPTCHA_PRIVATE_KEY=your_recaptcha_private_key
EMAIL_FROM=your_email
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password ```

## Features
- **User Authentication:** Implemented using django-allauth.
- **QR Code Generation:** Enabled through django-qr-code and segno.
- **User-Agent Parsing:** Managed by django-user-agents and ua-parser.
- **Captcha Verification:** Provided by django-recaptcha to prevent spam and abuse.
- **Email Account Recovery:** Allows users to recover their account via email.
- **Security:** Enhanced with argon2-cffi for password hashing and cryptography for secure communications.


