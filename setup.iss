; YaiZa-Pro Windows Installer
; Created with Inno Setup
; Run: iscc setup.iss

#define MyAppName "YaiZa Professional"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "YaiZa"
#define MyAppURL "https://github.com/yaimaza"
#define MyAppExeName "YaiZa-Pro.exe"
#define MyAppIconName "assets\icon.ico"

[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=output
OutputBaseFilename=YaiZa-Pro-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "thai"; MessagesFile: "compiler:Languages\Thai.isl"

[Types]
Name: "full"; Description: "Full installation"
Name: "compact"; Description: "Compact installation"
Name: "custom"; Description: "Custom installation"; Flags: iscustom

[Components]
Name: "program"; Description: "Program files"; Types: full compact custom; Flags: fixed
Name: "startmenu"; Description: "Start Menu shortcuts"; Types: full compact
Name: "desktopicon"; Description: "Desktop icon"; Types: full

[Files]
Source: "dist\YaiZa-Pro.exe"; DestDir: "{app}"; Components: program; Flags: ignoreversion
Source: "config\*"; DestDir: "{app}\config"; Components: program; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "assets\*"; DestDir: "{app}\assets"; Components: program; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; Components: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: dirifempty; Name: "{app}\config"
Type: dirifempty; Name: "{app}\assets"
Type: dirifempty; Name: "{app}"
