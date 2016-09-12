# LoklakHeatmap

[![Join the chat at https://gitter.im/loklak/loklak](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/loklak/loklak)

Tweet Heatmap using loklak as a source.


![Screenshot](https://cloud.githubusercontent.com/assets/3987198/18433618/f48d8a04-78e8-11e6-836d-85b231aeb5a0.png
)

Demo: <http://polbaladas.com/loklakHeatMap/>

##Set up / Requirements
Python Packages:
Flask 0.11.1
requests 2.10.0
Install with pip and requirements.txt.

## Local Set up

Install Requirements:
```pip install -r requirements.txt```

Run App:
```python main.py```

And the app should be running locally on port 5000 (127.0.0.0:5000) .

##Server set up

Install the app requirements just like in the local set up scenario.
Install your prefered server software (demo uses apache) and configure it to run the Flask App. 

DigitalOcean has a great tutorial to set up Flask apps with apache and nginx in an ubuntu environment:
<https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04> .

##License

GNU General Public License v3.0






