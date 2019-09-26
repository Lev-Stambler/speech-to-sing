import pydub
import numpy
import numpy.fft as fft

def save_mp3(data, rate, word):
  scipy.io.wavfile.write(f"sounds-music/{word}.wav", rate, data)

def read_mp3(f, normalized=False):
  """MP3 to numpy array"""
  a = pydub.AudioSegment.from_mp3(f)
  y = numpy.array(a.get_array_of_samples())
  if a.channels == 2:
    y = y.reshape((-1, 2))
  if normalized:
    return a.frame_rate, numpy.float32(y) / 2**15
  else:
    return a.frame_rate, y

def make_freq(word, note):
  sr, data = read_mp3(f"sounds/{word}.mp3")
  print(data)
  save_mp3(data, sr, word)



# spectrum = fft.fft(data)
#   freqs = fft.fftfreq(len(spectrum))

#   for coef,freq in zip(spectrum,freqs):
#     if coef:
#       print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,f=freq))
#   # freq = fft.fftfreq(len(spectrum)) * sr
#   # print(f"original frequency: {freq}")

