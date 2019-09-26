import sys
from gtts import gTTS
import os
import soundmanip
import wav_lib
import stitch
from pydub import AudioSegment

import re

def get_text(text_path):
  f = open(text_path, "r")
  contents = f.read()
  print("text path:", text_path)
  print("text contents: ", contents)
  f.close()
  return contents

def make_to_audio(words):
  for i, word in enumerate(words):
    if words.index(word) == i:
      tts = gTTS(text=word, lang='en')
      tts.save(f"sounds/{word}.mp3")
      os.system(f"mpg321 sounds/{word}.mp3")
      sound = AudioSegment.from_mp3(f"sounds/{word}.mp3")
      sound.export(f"sounds/{word}.wav", format="wav")

def get_words(text):
  return re.sub(r"[.,]", "", text).split(" ")

def main():
  time_step_ms = 1000
  notes = ["C4", "C4", "G5", "G5", "A5", "A5", "G5", "F5", "E5", "D5", "C4"]
  text_path = "words.txt"
  if len(sys.argv) > 1 and sys.argv[1] != "":
    text_path = sys.argv[1]
  text = get_text(text_path)
  words = get_words(text)
  # audio_words = make_to_audio(words)
  for i in range(0, len(notes)):
    duration = time_step_ms
    soundmanip.make_word(words[i], notes[i], duration, i)
  stitch.stitch(len(notes))

if __name__ == "__main__":
  main() 