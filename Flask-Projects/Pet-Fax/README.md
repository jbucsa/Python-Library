[![LinkedIn][linkedin-shield]][linkedin-url-Bucsa]

 
# Basic Flash Project

This project shows the basics tools for creating routes using Flask in Python. 


## Basic Launch STEP

1. Launch the VENV envirnoment 

```bash
venv\Scripts\activate.bat
```

2. Install pip
   
```bash
pip install python-dotenv

pip install Flask

pip install flask_sqlalchemy

pip install Flask-Migrate

pip install psycopg2-binary
```     

3. Database Migration
   
```bash
python -m flask db init             
python -m flask db migrate            
python -m flask db upgrade 
```

4. Launch Flask
   
```bash
python -m flask run
```

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url-Bucsa]: https://www.linkedin.com/in/justin-bucsa
