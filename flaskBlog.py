from flask import Flask ,render_template #inporting render_teplates functions from flask   #importing flask class from class module
app = Flask(__name__)     #creating flask instace

posts=[
    {'postTitle':'Post1',
        'authorName':'M Umer',
     'content':'post 1 content',
     'datePosted':'Dec 1,2020'
     },
    {
        'postTitle':'Post2',
        'authorName':'M Umer',
     'content':'post 1 content',
     'datePosted':'Dec 1,2020'
     },
]

@app.route('/')          # decorator funciton ,used to add additional functionality in existing functions
def hello_world():
    return '<H1>ksjdsdnckj</H1>'

@app.route('/home')          # decorator funciton ,used to add additional functionality in existing functions
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')          # decorator funciton ,used to add additional functionality in existing functions
def aboutPageFunc():
    return render_template('about.html',title='about')


if __name__== "__main__":
    app.run(debug=True)