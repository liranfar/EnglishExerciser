import os
import signal
from contextlib import contextmanager


class Voice:
    @classmethod
    def say(cls, sentence):

        if sentence is None:
            return

        try:
            with time_limit(2):

                from gtts import gTTS

                tts = gTTS(text=sentence, lang='en')
                temp_sound = '/tmp/temp.mp3'
                tts.save(temp_sound)
                from pygame import mixer

                mixer.init()
                mixer.music.load(temp_sound)
                mixer.music.play()
                os.remove(temp_sound)
        except TimeoutException as e:
            print("Timed out!")


class TimeoutException(Exception): pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
