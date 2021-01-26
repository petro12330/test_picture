# test_picture
git clone https://github.com/petro12330/test_picture.git 
mkdir test_picture\picture\media\images\resize  
virtualenv venv
venv\Scripts\activate.bat
pip install -r test_picture\requirements.txt
python manage.py makemigrations
python manage.py migrate
python test_picture\picture\manage.py runserver
python picture\manage.py runserver
