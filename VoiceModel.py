from gtts import gTTS
from io import BytesIO
import pygame

# สร้างข้อความพูด
text = "Hello world"
tts = gTTS(text=text, lang='en')

# สร้างไฟล์เสียงในหน่วยความจำ
audio_file = BytesIO()
tts.write_to_fp(audio_file)

# เล่นไฟล์เสียงโดยตรงจากหน่วยความจำ
audio_file.seek(0)  # เริ่มจากต้นของไฟล์

# เริ่มต้น pygame mixer
pygame.mixer.init()

# โหลดเสียงจากหน่วยความจำ
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()

# รอจนกว่าเสียงจะเล่นจบ
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
