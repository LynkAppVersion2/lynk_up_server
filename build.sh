python -m venv .venv
. .venv/bin/activate
cd lynk_up_server
pip install -r dependencies.txt
python manage.py migrate
