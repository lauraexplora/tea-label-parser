`sudo apt install -y libcap-dev libkms++-dev libfmt-dev libdrm-dev libcamera-dev tesseract-ocr tesseract-ocr-deu python3-dev`
`sudo raspi-config nonint do_i2c 0`
`python -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`
`pip install --no-dependencies rainbowhat`

## DEV: To uninstall all python packages
`pip cache purge && pip freeze | xargs pip uninstall -y`

