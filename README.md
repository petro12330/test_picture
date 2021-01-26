h1 README
-----------------------------------
h2 git clone https://github.com/petro12330/test_picture.git 
-----------------------------------
h2 mkdir test_picture\picture\media\images\resize  
-----------------------------------
h2 virtualenv venv
-----------------------------------
h2 venv\Scripts\activate.bat
-----------------------------------
h2 pip install -r test_picture\requirements.txt
-----------------------------------
h2 python test_picture\picture\manage.py makemigrations
-----------------------------------
h2 python test_picture\picture\manage.py migrate
-----------------------------------
h2 python test_picture\picture\manage.py runserver
-----------------------------------

