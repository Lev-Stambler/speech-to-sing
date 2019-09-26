import scipy.io.wavfile
import soundfile as sf

def save_wav(data, rate, path):
  scipy.io.wavfile.write(path, rate, data)

def open_wav(path):
  sr, data = scipy.io.wavfile.read(path)
  return sr, data

def wav_len_ms(path):
  f = sf.SoundFile(path)
  seconds = len(f) / f.samplerate
  return seconds * 1000