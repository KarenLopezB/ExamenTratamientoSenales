import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave

import matplotlib.pyplot as plt

#8769

frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1447, amp=1, offset=0)

#8
wave_852 = frecuencia852.make_wave(duration=0.5, start=0, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=0, framerate=44100)
#7
wave_852 = frecuencia852.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0.5, framerate=44100)
#6
wave_770 = frecuencia770.make_wave(duration=0.5, start=1, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=1, framerate=44100)
#9
wave_852 = frecuencia852.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido_8 = wave_852 + wave_1336
wave_sonido_7= wave_852 + wave_1209
wave_sonido_6 = wave_770 + wave_1477
wave_sonido_9 = wave_852 + wave_1477

wave_numfinal = wave_sonido_8 + wave_sonido_7 + wave_sonido_6 + wave_sonido_9

decorate(xlabel="Tiempo(s)")
decorate(ylabel="amplitud")

wave_numfinal.plot()
wave_numfinal.write("output8769.wav")
plt.show()