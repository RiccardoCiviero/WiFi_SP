mkdir %AppData%\CoreTech

robocopy . %AppData%\CoreTech -s

# TODO Change Exename
cd %AppData%\CoreTech
mklink /h "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\EXENAME" .\EXENAME