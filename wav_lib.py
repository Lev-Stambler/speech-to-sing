import scipy.io.wavfile

def save_wav(data, rate, path):
  scipy.io.wavfile.write(path, rate, data)

def open_wav(path):
    sr, data = scipy.io.wavfile.read(path)
    return sr, data