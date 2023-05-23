python -m venv .venv
. .venv/bin/activate
cd lynk_up_server
python manage.py migrate --no-input
pip install -r dependencies.txt
