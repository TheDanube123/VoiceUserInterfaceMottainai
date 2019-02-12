import subprocess

class TTS:
    """Set TTS functions. by 150513 komatani"""

    def __init__ (self):
#        self.TTScmd = "ruby voicetext.rb; play output.wav 2> /dev/null"
#        self.TTScmd = "ruby aitalk.rb; play output.wav 2> /dev/null"
        self.TTScmd = "say -f -"

    def callTTS(self, text):
        cmd = "echo " + text + " | " + self.TTScmd
        subprocess.call(cmd, shell=True)
