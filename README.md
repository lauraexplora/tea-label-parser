`sudo apt install libcap-dev libkms++-dev libfmt-dev libdrm-dev libcamera-dev tesseract-ocr tesseract-ocr-deu`
`python -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`
`pip install --no-dependencies rainbowhat`

## DEV: To uninstall all python packages
`pip cache purge && pip freeze | xargs pip uninstall -y`

