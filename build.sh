# build.sh
pip install -r requirements.txt
python3.9 manage.py collectstatic
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', '12345678')" | python3.9 manage.py shell