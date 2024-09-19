source venv/bin/activate
pip install --upgrate pip
pip install -r requirements.txt
rm -rf public
reflex init
#API_URL=https://dockercrey.up.railway.app/ 
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivated