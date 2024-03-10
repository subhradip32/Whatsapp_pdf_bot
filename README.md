# WhatsApp to PDF Converter

## Overview
This Flask application provides functionality to convert images sent via WhatsApp to a PDF document. Users can send images through WhatsApp, and the application will download and convert them into a PDF file.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/subhradip32/Whatsapp_pdf_bot.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up a Twilio account and obtain the Account SID and Auth Token. Update the `account_sid` and `auth_token` variables in the code with your credentials.
4. Ensure that you have Flask installed. If not, install it using:
   ```bash
   pip install Flask
   ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Expose the application to the internet using tools like ngrok.
3. Configure your Twilio WhatsApp Sandbox to forward messages to the ngrok URL.
4. Send images through WhatsApp to the configured Twilio number with the message ".pdf" to receive a PDF containing the images.

## Features
- Convert images sent via WhatsApp to a single PDF document.
- Automatically generate unique filenames for downloaded images.
- Error handling for unreadable files and invalid requests.

## Dependencies
- [Flask](https://pypi.org/project/Flask/): Flask is a lightweight WSGI web application framework for Python.
- [twilio](https://www.twilio.com/docs/): Twilio is a cloud communications platform as a service company. The `twilio` Python module allows interfacing with the Twilio API for sending and receiving messages.
- [requests](https://pypi.org/project/requests/): Requests is a simple HTTP library for making requests in Python.
- [img2pdf](https://pypi.org/project/img2pdf/): img2pdf is a Python library for converting images to PDF format.
- [pathlib](https://docs.python.org/3/library/pathlib.html): pathlib is a module providing object-oriented filesystem paths.

## Contributing
Contributions are welcome! If you encounter any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
