from selenium import webdriver

driver_location = '/media/jisan/C48458B38458A9A6/Web/chromedriver'
binary_location = '/usr/bin/google-chrome'

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location,options=options)
driver.get("https://www.youtube.com/watch?v=67h3IT2lm40")

connected pyuno with libreoffice
created extension with pyuno
added and tested extension with pyuno
Started developing extension UI as requirement

python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'dialogs_files' -d '/home/jisan/.config/libreoffice/4/user/Scripts/python/TestLib' -a 'Test_dialogs'

python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'dialogs_oxt' -d '/home/jisan/.config/libreoffice/4/user/Scripts/python/TestLib' -a 'Test_dialogs'


Complete the remaining part of libreoffice extension
Complete the remaining fixes of libreoffice extension UI as requiremnet
Create a deployable version of the extension

 path1='~/.config/libreoffice/4/user/basic/Standard/Dialog1.xdl'
 path2='~/.config/libreoffice/4/user/basic/Standard/Dialog2.xdl'
 path3='~/.config/libreoffice/4/user/basic/Standard/Dialog3.xdl'


python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'sidebar_convert' -d '/home/jisan/.config/libreoffice/4/user/Scripts/python/TestLib' -a 'Test_sidebar' -p 1






sudo cp ~/Documents/test.xdl  /home/jisan/.config/libreoffice/4/user/Scripts/python
sudo cp /home/jisan/Documents/unodit-master/config.ini  /usr/lib/python3.10/unodit/unodit-master
sudo cp /home/jisan/Documents/unodit-master/config.ini /home/jisan/.config/libreoffice/4/user/Scripts/python/TestLib
sudo cp /home/jisan/Downloads/unodit-master/*  /usr/lib/python3.10/unodit/uno

/home/jisan/Documents/unodit-master/config.ini


python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'sidebar_convert' -d '/home/jisan/.config/4/user/Scripts/python/TestLib' -a 'Test_sidebar' -p 2

python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'sidebar_files' -d '/home/jisan/.config/4/user/Scripts/python/TestLib' -a 'Test_sidebar' -p 2

python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'sidebar_oxt' -d '/home/jisan/.config/4/user/Scripts/python/TestLib' -a 'Test_sidebar' -p 2

Uccharon-Final.xdl
sudo rm config.ini

1.Completed sending texts on chunks
2.Completed TTS microsoft office extension
3.Deployed TTS extension and created package of the extension
4.Started development of libre office plugin


/home/jisan/Documents/uccharon2.xdl


python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'script_convert' -d '/home/jisan/.config/4/user/Scripts/python/TestLib' -f '/home/jisan/Documents/Uccharon-Final.xdl' -a 'Request'

python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'script_convert' -d '/home/jisan/.config/4/user/Scripts/python/addon' -f '/home/jisan/Documents/tts_close_button.xdl' -a 'tts'



python3 /home/reve/Desktop/unodit-master/unodit.py  -m 'script_convert' -d '/home/reve/.config/4/user/Scripts/python/previous' -f '/home/reve/Documents/tts_refined.xdl' -a 'ttsfinal'
python3 /home/reve/Desktop/unodit-master/unodit.py  -m 'script_files'   -d '/home/reve/.config/4/user/Scripts/python/previous' -f '/home/reve/Documents/tts_refined.xdl' -a 'ttsfinal'
python3 /home/reve/Desktop/unodit-master/unodit.py  -m 'script_oxt'     -d '/home/reve/.config/4/user/Scripts/python/previous' -f '/home/reve/Documents/tts_refined.xdl' -a 'ttsfinal'


python3 /home/reve/Desktop/unodit-master/unodit.py  -m 'script_convert' -d '/home/reve/.config/4/user/Scripts/python/STTT' -f '/home/reve/Documents/stt_v1.xdl' -a 'stt_v1'
python3 /home/reve/Desktop/unodit-master/unodit.py -m 'script_files'    -d '/home/reve/.config/4/user/Scripts/python/STTT' -f '/home/reve/Documents/stt_v1.xdl' -a 'stt_v1'
python3 /home/reve/Desktop/unodit-master/unodit.py  -m 'script_oxt'     -d '/home/reve/.config/4/user/Scripts/python/STTT' -f '/home/reve/Documents/stt_v1.xdl' -a 'stt_v1'


python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'script_convert' -d '/home/jisan/.config/4/user/Scripts/python/addon' -f '/home/jisan/Documents/tts_close_button.xdl' -a 'ttss'
python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'script_files'   -d '/home/jisan/.config/4/user/Scripts/python/addon' -f '/home/jisan/Documents/tts_close_button.xdl' -a 'ttss'
python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'script_oxt'     -d '/home/jisan/.config/4/user/Scripts/python/addon' -f '/home/jisan/Documents/tts_close_button.xdl' -a 'ttss'





python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'script_convert' -d '/home/jisan/.config/4/user/Scripts/python/addon' -f '/home/jisan/Documents/checkRadio.xdl' -a 'testradio'
python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'script_files'   -d '/home/jisan/.config/4/user/Scripts/python/addon' -f '/home/jisan/Documents/checkRadio.xdl' -a 'testradio'
python3 /usr/lib/python3.10/unodit/unodit-master/unodit.py -m 'script_oxt'     -d '/home/jisan/.config/4/user/Scripts/python/addon' -f '/home/jisan/Documents/checkRadio.xdl' -a 'testradio'



Completed UI design for libreoffice plugin development
integrated UI with Backend
Converted ANSI to Unicode
Working on dynamicly fetching data from document to backend


python3 /home/reve/Desktop/unodit-master/unodit.py -m 'dialogs_create' -d '/home/jisan/.config/4/user/Scripts/python/addon' -a 'STT'
python3 /home/reve/Desktop/unodit-master/unodit.py -m 'dialogs_files'  -d  '/home/jisan/.config/4/user/Scripts/python/addon' -a 'STT'
python3 /home/reve/Desktop/unodit-master/unodit.py -m 'dialogs_oxt'  -d  '/home/jisan/.config/4/user/Scripts/python/addon' -a 'STT'


python3 /home/reve/Desktop/unodit-master/unodit.py -m 'dialogs_create' -d '/home/reve/.config/4/user/Scripts/python/third' -a 'Test_dialogs'
python3 /home/reve/Desktop/unodit-master/unodit.py -m 'dialogs_files'  -d  '/home/reve/.config/4/user/Scripts/python/third' -a 'Test_dialogs'
python3 /home/reve/Desktop/unodit-master/unodit.py -m 'dialogs_oxt'  -d  '/home/reve/.config/4/user/Scripts/python/third' -a 'Test_dialogs'


os.system("pip install pydub")


python3 /home/reve/Desktop/unodit-master/unodit.py -m 'script_convert' -d '/home/reve/Downloads/STT1' -f '/home/reve/Documents/stt_v1.xdl' -a 'stt_writer'
python3 /home/reve/Desktop/unodit-master/unodit.py -m 'script_files'   -d '/home/reve/Downloads/STT1' -f '/home/reve/Documents/stt_v1.xdl' -a 'stt_writer'
python3 /home/reve/Desktop/unodit-master/unodit.py -m 'script_oxt'     -d '/home/reve/Downloads/STT1'  -f '/home/reve/Documents/stt_v1.xdl' -a 'stt_writer'



python3 /home/reve/Desktop/unodit-master/unodit.py -m 'script_convert' -d '/media/reve/New Volume/Unodit/TTS-Libre/tts_libre_office_text_document_addin2' -f '/home/reve/Documents/tts_refined.xdl' -a 'tts_writer'
python3 /home/reve/Desktop/unodit-master/unodit.py -m 'script_files'   -d '/media/reve/New Volume/Unodit/TTS-Libre/tts_libre_office_text_document_addin2' -f '/home/reve/Documents/tts_refined.xdl' -a 'tts_writer'

python3 /home/reve/Desktop/unodit-master/unodit.py -m 'script_oxt'   -d '/media/reve/New Volume/Unodit/TTS-Libre/tts_libre_office_text_document_addin2' -f '/home/reve/Documents/tts_refined.xdl' -a 'tts_writer'

started working on streming feature of STT microsoft office word addin

cd

soffice "--accept=socket,host=127.0.0.1,port=2002,tcpNoDelay=1;urp;StarOffice.ComponentContext" --norestore


python3 /home/reve/Desktop/unodit-master/unodit.py -m 'script_convert' -d '/media/reve/New Volume/Unodit/TTS-Libre/tts_libre_office_text_document_addin2' -f '//media/reve/New Volume/Text' -a 'tts_writer'
python3 /home/reve/Desktop/unodit-master/unodit.py -m 'script_files'   -d '/media/reve/New Volume/Unodit/TTS-Libre/tts_libre_office_text_document_addin2' -f '/home/reve/Documents/tts_refined.xdl' -a 'tts_writer'

python3 /home/jisananm/Desktop/unodit-master/unodit.py -m 'script_convert'   -d '/media/jisananm/New Volume/Test2' -f '/home/jisananm/Documents/image.xdl' -a 'tts_image'
python3 /home/jisananm/Desktop/unodit-master/unodit.py -m 'script_files'     -d '/media/jisananm/New Volume/Test2' -f '/home/jisananm/Documents/image.xdl' -a 'tts_image'
python3 /home/jisananm/Desktop/unodit-master/unodit.py -m 'script_oxt'       -d '/media/jisananm/New Volume/Test2' -f '/home/jisananm/Documents/image.xdl' -a 'tts_image'

/media/reve/New Volume/Text

/home/reve/Downloads/download.png 
/media/jisananm/New Volume/Test2/Images/image.png
