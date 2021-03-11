mkdir %AppData%\CoreTech

robocopy . %AppData%\CoreTech -s

cd %AppData%\CoreTech

REM Installing SW dependencies
ECHO Setting up Firefox...
IF exist "C:\Program Files\Mozilla Firefox" ( echo Firefox already installed ) ELSE ( .\sw\FirefoxInstaller.exe)
REM IF exist "C:\Users\leona\AppData\Roaming\Python\Python39" ( echo Python already installed ) ELSE ( .\sw\python-3.9.2-amd64.exe)
ECHO Setting up GekoDriver...
pathman /au %AppData%\CoreTech\sw

REM Add to shell:startup
mklink /h "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\WiFiSP.exe" .\WiFiSP.exe

WifiSPsetup.exe