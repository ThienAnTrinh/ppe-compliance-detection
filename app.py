from flask import Flask, render_template, Response, session
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import os
import cv2
from detect import video_detection


app = Flask(__name__)

app.config['SECRET_KEY'] = 'thien'
app.config['UPLOAD_FOLDER'] = 'static/files'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Run")


def generate_frames(path=''):
    output = video_detection(path)
    for detection_ in output:
        ref, buffer = cv2.imencode('.jpg', detection_)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')


def generate_frames_web(path=0):
    yolo_output = video_detection(path)
    for detection_ in yolo_output:
        ref, buffer = cv2.imencode('.jpg', detection_)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    session.clear()
    return render_template('index.html')


@app.route("/webcamPage", methods=['GET', 'POST'])
def webcam_page():
    session.clear()
    return render_template('webcam.html')


@app.route('/videoPage', methods=['GET', 'POST'])
def video_page():
    # Upload File Form: Create an instance for the Upload File Form
    form = UploadFileForm()
    if form.validate_on_submit():
        # Our uploaded video file path is saved here
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename))
                  )
        # Use session storage to save video file path
        session['video_path'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                             app.config['UPLOAD_FOLDER'],
                                             secure_filename(file.filename))

    return render_template('video.html', form=form)


@app.route('/video')
def video():
    return Response(generate_frames(path=session.get('video_path', None)), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/webcam')
def webcam():
    return Response(generate_frames_web(path=0), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
