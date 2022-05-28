#Do this: everytime that you install a new package
#pip3 freeze > requirements.txt 
#source venv/bin/activate
#python run.py

from website import create_app

app = create_app()

if __name__ == "__main__": #only if we run this file you run the webapplication
    app.run(debug=True) 
    