mkdir %AppData%\CoreTech

robocopy . %AppData%\CoreTech -s

cd %AppData%\CoreTech
mklink /h "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\WiFiSP.exe" .\WiFiSP.exe

WifiSPsetup.exe