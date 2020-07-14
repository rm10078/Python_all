from gtts import gTTS
import os
text="Hey i am pretty genius liza" 
language="en"
speech=gTTS(text=text, lang=language, slow=False)
speech.save("liz.mp3")
os.system("liz.mp3")