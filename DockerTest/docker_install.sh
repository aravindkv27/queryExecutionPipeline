virtualenv --python=/usr/bin/python3.10 kebsQE
source kebsQE/bin/activate
pip install -r requirements.txt -t kebsQE/lib/python3.10/site-packages
zip -r9 kebsQE.zip kebsQE
