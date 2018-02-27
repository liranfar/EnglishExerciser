import os


class Voice():

    @classmethod
    def say(cls, sentence):

        if sentence is None:
            return

        from gtts import gTTS
        tts = gTTS(text=sentence, lang='en')
        temp_sound = '/tmp/temp.mp3'
        tts.save(temp_sound)
        from pygame import mixer
        mixer.init()
        mixer.music.load(temp_sound)
        mixer.music.play()
        os.remove(temp_sound)