; YaiZa-Pro Inno Setup Installer Script
; Creates a professional Windows installer (.exe)

[Setup]
AppName=YaiZa-Pro
AppVersion=1.0.0
AppPublisher=YaiZa Professional
AppPublisherURL=https://github.com/yaimaza/
DefaultDirName={commonpf}\YaiZa-Pro
DefaultGroupName=YaiZa-Pro
OutputDir=dist
OutputBaseFilename=YaiZa-Pro-1.0.0-Setup
SetupIconFile=assets\icon.ico
UninstallDisplayIcon={app}\assets\icon.ico
LicenseFile=LICENSE.txt
PrivilegesRequired=admin
ShowLanguageDialog=yes

[Languages]
Name: en; MessagesFile: "compiler:Default.isl"
Name: th; MessagesFile: "compiler:Languages\Thai.isl"

[Messages]
WelcomeLabel1=Welcome to YaiZa-Pro Setup
WelcomeLabel2=This will install YaiZa-Pro v1.0.0 on your computer.%n%nYaiZa-Pro is an AI-powered Network CCTV Automation system.

[Files]
Source: "main.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "app\*"; DestDir: "{app}\app"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "config\*"; DestDir: "{app}\config"; Flags: ignoreversion
Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion
Source: "requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion

[Dirs]
Name: "{app}\logs"
Name: "{app}\data"
Name: "{app}\config"

[Icons]
Name: "{group}\YaiZa-Pro"; Filename: "{app}\main.py"; IconFilename: "{app}\assets\icon.ico"
Name: "{group}\Uninstall YaiZa-Pro"; Filename: "{uninstallexe}"
Name: "{commondesktop}\YaiZa-Pro"; Filename: "{app}\main.py"; IconFilename: "{app}\assets\icon.ico"

[Run]
Filename: "{app}\requirements.txt"; Description: "Install Dependencies"; Flags: shellexec postinstall skipifsilent
Filename: "{app}\README.md"; Description: "View README"; Flags: shellexec postinstall skipifsilent unchecked

[UninstallDelete]
Type: dirifempty; Name: "{app}"
