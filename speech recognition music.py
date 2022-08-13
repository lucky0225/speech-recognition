import pyglet
import wave
import pyaudio
import speech_recognition as sr


def play_audio(filename):
    # chunk indicates the size of "filename"
    chunk = 1024
    wf = wave.open(filename, "rb")
    pa = pyaudio.PyAudio()

    # load data into a stream (pyaudio)
    stream = pa.open(
        # get format, channels, framerate of the file
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    # define data_stream
    data_stream = wf.readframes(chunk)

    # while there is "data_stream" -> continue reading
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

# play_audio("./rocket2.wav")

# recognizing speech
r = sr.Recognizer()

def initSpeech():
    while True:

        print("Starting...")
        play_audio("./upset-sound-tone.wav")
        # defining microphone as source to listen to
        with sr.Microphone() as source:
            print("Choose from the following:\n - music\n - stop")
            audio = r.listen(source)
        play_audio("./rocket2.wav")
        recorded_audio = ""
        try:
            # can use different engines to recognize speech
            # english only
            recorded_audio = r.recognize_google(audio)
        except:
            print("No audio recognized, please repeat")

        audio_signal = recorded_audio.split(" ")
        # if successful 
        print("Recorded: ", recorded_audio)
        print("Signal", audio_signal)

        # testing for "music"
        if "music" in audio_signal:
            play_audio("./violin.wav")
            print("Which music do you want to listen to? You can choose between:\n - rock\n - pop\n - classic")
            with sr.Microphone() as source:
                audio =r.listen(source)
                recorded_audio = ""
            try:
                recorded_audio = r.recognize_google(audio)
            except:
                print("No audio recognized, please repeat")

            audio_signal = recorded_audio.split(" ")
            print("Recorded: ", recorded_audio)
            print("Signal", audio_signal)

            if "rock" in audio_signal:
                play_audio("./Rammstein.wav")
            elif "pop" in audio_signal:
                play_audio("./Sinatra.wav")
            elif "classic" in audio_signal:
                play_audio("./Mozart.wav")
            else:
                print("Could not recognize music")
        
        if "stop" in audio_signal:
            print("Program stops")
            exit()



print(initSpeech())

# improvisation
#   while loop for recording
#   if "name" was called -> activate
#   test for "play music", "music", "band name" etc -> play music

"""
#  play sound
file = pyglet.resource.media("upset-sound-tone.mp3")
file.play()

pyglet.app.run()
"""

# wave supports the WAV sound format which supports mono and stereo 
# https://docs.python.org/3/library/wave.html           # wave
# https://pyglet.readthedocs.io/en/latest/              # pyglet
# https://people.csail.mit.edu/hubert/pyaudio/docs/     # pyaudio

# error "format= 65534"
# https://online-audio-converter.com/
# change channel to 1
# https://forum.defold.com/t/sound-warning-what-is-pcm-format-1-solved/63595