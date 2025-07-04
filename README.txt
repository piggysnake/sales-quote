README.txt
change and run the app

curtain_cal.py:
replacements included all words that can be translated to english
not smart enough to regonize: Sfold curtain, Sfold sheer, Pinch curtain, Pinch sheer. calculation will include all anwser
unable to provide a subtotal

   *note:
  	roller blinds is rounded to 1000w and 1000h
  	void window does not include roller blinds
  	all anwser rounded to floor, eg 265.89 -> 265, 213.11 -> 213
  

setup.py 
use to set up the app
test:
   platform limitation might exist
   create a website can be another solution
   icon availabel for diy if needed.

method of fixing and rebuild:
rm -rf build dist *.egg-info
python3 Desktop/Ben_quote/setup.py py2app
