python -m venv .venv
. .venv/bin/activate
cd lynk_up_server
pip install -r dependencies.txt
python manage.py makemigrations
python manage.py migrate --no-input
