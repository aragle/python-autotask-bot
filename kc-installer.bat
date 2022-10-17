@ECHO OFF
git clone https://github.com/aratheunseen/kormochari.git
cd kormochari
pip install .
cd ..
rmdir /S /Q kormochari
echo Library Install Successful. >> kc-info.txt
echo. >> kc-info.txt
echo To check the library: >> kc-info.txt
echo. >> kc-info.txt
echo	Type 'pip show kormochari' in Command Prompt(CMD). >> kc-info.txt
echo. >> kc-info.txt
echo. >> kc-info.txt
echo Thanks for installing kormochari. >> kc-info.txt
echo. >> kc-info.txt
echo ~ Ashiqur Rahman Alif (aratheunseen) >> kc-info.txt
echo ~ GitHub: https://github.com/aratheunseen  >> kc-info.txt
del kc-installer.bat
exit