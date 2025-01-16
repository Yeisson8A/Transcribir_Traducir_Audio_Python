# -*- coding: utf-8 -*-
"""Transcribir_Traducir_Audio_Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tGUHCCeCXJKuM_VU3fGAdk6GlD3--nw4

**Transcribir y traducir el audio a partir de un video**
"""

!pip install moviepy

!pip install openai-whisper

!apt-get install -y ffmpeg

!pip install deep-translator

!pip install gTTS

from google.colab import drive
drive.mount('/content/drive')

import whisper
import os
from moviepy.editor import AudioFileClip
from deep_translator import GoogleTranslator
from gtts import gTTS
from IPython.display import Audio

# Definir función para convertir video a audio
def from_video_to_audio(video_path, output_ext="wav"):
    # Obtener la ruta del directorio, nombre del archivo sin extensión y construir la nueva ruta
    base_path, file_name = os.path.split(video_path)  # Separa la ruta y el nombre del archivo
    name_without_ext, _ = os.path.splitext(file_name)  # Extrae el nombre sin extensión
    # Construir la ruta completa del archivo de salida con la nueva extensión
    audio_output = os.path.join(base_path, f"{name_without_ext}.{output_ext}")
    # Extraer y guardar el audio
    audio_clip = AudioFileClip(video_path)
    audio_clip.write_audiofile(audio_output)
    audio_clip.close()  # Asegura cerrar el recurso
    print(f"Audio almacenado en: {audio_output}")
    return audio_output

# Definir función para convertir texto a audio
def from_text_to_audio(text, lang, new_path):
  # Obtener la ruta del directorio, nombre del archivo sin extensión y construir la nueva ruta
  base_path, file_name = os.path.split(new_path)  # Separa la ruta y el nombre del archivo
  name_without_ext, _ = os.path.splitext(file_name)  # Extrae el nombre sin extensión
  # Construir la ruta completa del archivo de salida con la nueva extensión
  audio_output = os.path.join(base_path, f"{name_without_ext}_{lang}.mp3")
  # Generar archivo de audio
  tts = gTTS(text, lang=lang)
  tts.save(audio_output)
  return audio_output

# Establecer el modelo que se va a usar
model = whisper.load_model("base")

"""***Inglés***"""

# Llamar función
video_path = "/content/drive/MyDrive/Cursos/Python 2024/Transcribir audio/Video_2.mp4"
audio_path = from_video_to_audio(video_path)

Audio(audio_path, autoplay=True)

# Transcribir audio
result = model.transcribe(audio_path)
print(result["text"])

# Traducir texto del audio
translated = GoogleTranslator(source='auto', target='es').translate(result["text"])
print(translated)

# Llamar función nuevo audio traducido
translate_audio_path = from_text_to_audio(translated, 'es', audio_path)

Audio(translate_audio_path, autoplay=True)

# Llamar función
video_path = "/content/drive/MyDrive/Cursos/Python 2024/Transcribir audio/Video_1.mp4"
audio_path = from_video_to_audio(video_path)

Audio(audio_path, autoplay=True)

# Transcribir audio
result = model.transcribe(audio_path)
print(result["text"])

# Traducir texto del audio
translated = GoogleTranslator(source='auto', target='es').translate(result["text"])
print(translated)

# Llamar función nuevo audio traducido
translate_audio_path = from_text_to_audio(translated, 'es', audio_path)

Audio(translate_audio_path, autoplay=True)

"""**Transcribir y traducir a partir de un audio**

***Francés***
"""

audio_path = "/content/drive/MyDrive/Cursos/Python 2024/Transcribir audio/Audio_2.mp3"
Audio(audio_path, autoplay=True)

# Transcribir audio
result = model.transcribe(audio_path)
print(result["text"])

# Traducir texto del audio
translated = GoogleTranslator(source='auto', target='es').translate(result["text"])
print(translated)

# Llamar función nuevo audio traducido
translate_audio_path = from_text_to_audio(translated, 'es', audio_path)

Audio(translate_audio_path, autoplay=True)

audio_path = "/content/drive/MyDrive/Cursos/Python 2024/Transcribir audio/Audio_1.mp3"
Audio(audio_path, autoplay=True)

# Transcribir audio
result = model.transcribe(audio_path)
print(result["text"])

# Traducir texto del audio
translated = GoogleTranslator(source='auto', target='es').translate(result["text"])
print(translated)

# Llamar función nuevo audio traducido
translate_audio_path = from_text_to_audio(translated, 'es', audio_path)

Audio(translate_audio_path, autoplay=True)

"""***Italiano***"""

audio_path = "/content/drive/MyDrive/Cursos/Python 2024/Transcribir audio/Audio_3.mp3"
Audio(audio_path, autoplay=True)

# Transcribir audio
result = model.transcribe(audio_path)
print(result["text"])

# Traducir texto del audio
translated = GoogleTranslator(source='auto', target='es').translate(result["text"])
print(translated)

# Llamar función nuevo audio traducido
translate_audio_path = from_text_to_audio(translated, 'es', audio_path)

Audio(translate_audio_path, autoplay=True)

audio_path = "/content/drive/MyDrive/Cursos/Python 2024/Transcribir audio/Audio_4.mp3"
Audio(audio_path, autoplay=True)

# Transcribir audio
result = model.transcribe(audio_path)
print(result["text"])

# Traducir texto del audio
translated = GoogleTranslator(source='auto', target='es').translate(result["text"])
print(translated)

# Llamar función nuevo audio traducido
translate_audio_path = from_text_to_audio(translated, 'es', audio_path)

Audio(translate_audio_path, autoplay=True)

"""***Portugués***"""

audio_path = "/content/drive/MyDrive/Cursos/Python 2024/Transcribir audio/Audio_5.mp3"
Audio(audio_path, autoplay=True)

# Transcribir audio
result = model.transcribe(audio_path)
print(result["text"])

# Traducir texto del audio
translated = GoogleTranslator(source='auto', target='es').translate(result["text"])
print(translated)

# Llamar función nuevo audio traducido
translate_audio_path = from_text_to_audio(translated, 'es', audio_path)

Audio(translate_audio_path, autoplay=True)

audio_path = "/content/drive/MyDrive/Cursos/Python 2024/Transcribir audio/Audio_6.mp3"
Audio(audio_path, autoplay=True)

# Transcribir audio
result = model.transcribe(audio_path)
print(result["text"])

# Traducir texto del audio
translated = GoogleTranslator(source='auto', target='es').translate(result["text"])
print(translated)

# Llamar función nuevo audio traducido
translate_audio_path = from_text_to_audio(translated, 'es', audio_path)

Audio(translate_audio_path, autoplay=True)