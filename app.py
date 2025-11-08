from flask import Flask, render_template, request
import os
from modules.queue import Queue
from modules.dequeue import DeQueue

app = Flask(__name__)

# Home page
@app.route('/')
@app.route('/home')
def index():
    index_data = {
        "message": "GROUP 11",
        "message_1": "Hello everyone we are the Group 11 and this is our Group Portfolio project in DSA"
    }
    return render_template('home.html', index=index_data, active_page='home')

# Projects page
@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html', active_page='works')

# Members / Contact page
@app.route('/contacts')
def members_contact():
    people = [
        {
            "name": "Mark Christian Abucejo",
            "image": "static/images/pic_1.png",
            "links": {
                "facebook": "https://www.facebook.com/mrkchrstnsbcj",
                "email": "https://www.facebook.com/mrkchrstnsbcj",
                "github": "https://github.com/nug3tsss",
            }
        },
        {
            "name": "Zy Banez",
            "image": "static/images/zy.jpg",
            "links": {
                "facebook": "https://www.facebook.com/zyescote.banez.5",
                "email": "zyescotebanez@gmail.com",
                "github": "https://github.com/ITZMEXYZ",
            }
        },
        {
            "name": "Kyle Isaac Celin",
            "image": "static/images/pic_2.png",
            "links": {
                "facebook": "https://www.facebook.com/cee.the.lin.e",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://github.com/ceetheline",
            }
        },
        {
            "name": "John Luke Fabillan",
            "image": "static/images/pic_3.png",
            "links": {
                "facebook": "https://www.facebook.com/johnluke.fabillan",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://github.com/JLFabillan",
            }
        },
        {
            "name": "Princess Sophia Manalo",
            "image": "static/images/pic_4.png",
            "links": {
                "facebook": "https://www.facebook.com/soapymk",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://github.com/Sophia18",
            }
        },
        {
            "name": "Isaac Christian Pelingen",
            "image": "static/images/pic_5.png",
            "links": {
                "facebook": "https://www.facebook.com/isaac.christian.pelingen",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://github.com/xiin112",
            }
        },
        {
            "name": "Gian Carlos Tumanan",
            "image": "static/images/pic_6.png",
            "links": {
                "facebook": "https://www.facebook.com/giancarlos.tumanan",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://github.com/GIANT0808",
            }
        }
    ]
    return render_template("contacts.html", people=people)

# Queue Visualizer page
@app.route('/works/queue-visualizer', methods=['GET', 'POST'])
def queue_visualizer():
    return render_template('queuevisualizer.html')

# DeQueue Visualizer page
@app.route('/works/dequeue-visualizer', methods=['GET', 'POST'])
def dequeue_visualizer():
    return render_template('dequeuevisualizer.html')
