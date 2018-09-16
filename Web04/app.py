from flask import*
import mlab
from youtube_dl import YoutubeDL
from models.video import Video
from models.account import Account

app = Flask(__name__)
app.secret_key = "a super super secret key"

mlab.connect()

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos = videos)

@app.route('/detail/<youtube_id>')
def detail():
    return render_template('detail.html',youtube_id = youtube_id) 

@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        
        if username == 'admin' and password == 'admin':
            session['loggedin'] = True
            return redirect(url_for('admin'))
        else:
            return 'Sai tên tài khoản và mật khẩu'
    
# @app.route('/admin', methods =["GET", "POST"])
# def admin():
#     if "loggedin" in session:
#         if session['loggined'] = True:
#             if request.method == "GET":
#                 videos = Video.objects()
#                 return render_template('admin.html', videos = videos)
#             elif request.method == "POST":
#                 form = request.form
#                 link = form['link'] 

#             ydl = YoutubeDL()


#         data = ydl.extract_info(link ,download = False)

#         title = data['title']
#         views = data['view_count']
#         thumbnail = data['thumbnail']
#         youtube_id = data ['id']

#         video = Video (
#             title = title,
#             views = views,
#             thumbnail = thumbnail,
#             youtube_id = youtube_id,
#             link = link
#         )

#         video.save()

#         return redirect(url_for('admin'))

@app.route('/logout')   
def logout():
    session['loggedin'] = False
    return redirect(url_for('index'))       

@app.route('/sign-in', methods = ["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('sign-in.html')
    elif request.method == "POST":

        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']

        new_account = Account (
            fullname = fullname,
            email = email,
            username = username,
            password = password
        )
        
        new_account.save()
        return "Sign up Finished"

    

if __name__ == '__main__':
  app.run(debug=True)
 