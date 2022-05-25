###this file maked for measurement PESQ score




import soundfile as sf
from pypesq import pesq

ref, sr = sf.read("./demo_data/test/noisy_voice_long_all.wav")
deg, sr = sf.read("./demo_data/save_predictions_all/denoise_all.wav")

cut = int((len(ref)/4))
ref2 = ref[0:cut]
print("all score")
score = pesq(deg, ref2,  sr)


print(score)
##############################################################################
#ref, sr = sf.read("./demo_data/test/noisy_voice_long_metro.wav")
#deg, sr = sf.read("./demo_data/save_predictions_metro/denoise_metro.wav")
#
#cut = int((len(ref)/4))
#ref2 = ref[0:cut]
#print("metro score")
#score = pesq(deg,ref2,  sr)
#
#
#print(score)
###########################################################################
#ref, sr = sf.read("./demo_data/test/noisy_voice_long_park.wav")
#deg, sr = sf.read("./demo_data/save_predictions_park/denoise_park.wav")
#
#cut = int((len(ref)/4))
#ref2 = ref[0:cut]
#print("park score")
#score = pesq(deg,ref2, sr)
#
#
#print(score)
#################################################################################

#ref, sr = sf.read("./demo_data/test/noisy_voice_long_street2.wav")
#deg, sr = sf.read("./demo_data/save_predictions_street/denoise_street2.wav")
#
#cut = int((len(ref)/4))
#ref2 = ref[0:cut]
#print("street score")
#score = pesq(deg,ref2, sr)
#
#
#print(score)