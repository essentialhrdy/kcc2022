import librosa
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from data_tools import scaled_in, inv_scaled_ou
from data_tools import audio_files_to_numpy, numpy_audio_to_matrix_spectrogram, matrix_spectrogram_to_numpy_audio


X_pred = loaded_model.predict(X_in)
print("1")
#Rescale back the noise model
inv_sca_X_pred = inv_scaled_ou(X_pred)
print("1")
#Remove noise model from noisy speech
X_denoise = m_amp_db_audio - inv_sca_X_pred[:,:,:,0]
#Reconstruct audio from denoised spectrogram and phase
print(X_denoise.shape)
print(m_pha_audio.shape)
print(frame_length)
print(hop_length_fft)
audio_denoise_recons = matrix_spectrogram_to_numpy_audio(X_denoise, m_pha_audio, frame_length, hop_length_fft)
#Number of frames
nb_samples = audio_denoise_recons.shape[0]
#Save all frames in one file
denoise_long = audio_denoise_recons.reshape(1, nb_samples * frame_length)*10
librosa.output.write_wav(dir_save_prediction + audio_output_prediction, denoise_long[0, :], sample_rate)