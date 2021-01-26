# test_picture
git clone https://github.com/petro12330/test_picture.git 
mkdir picture\media\images\resize  
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python test_picture\picture\manage.py runserver
python picture\manage.py runserver
