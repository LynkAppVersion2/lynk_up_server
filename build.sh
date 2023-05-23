python -m venv .venv
. .venv/bin/activate
cd lynk_up_server
pip install -r lynk_up_server/dependencies.txt
python manage.py migrate --no-input
