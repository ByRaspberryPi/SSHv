@echo off
powershell -Command "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"
TIMEOUT 3
powershell -Command "
Start-Service sshd;
Set-Service -Name sshd -StartupType 'automatic';
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH server (sshd)' -Enabled true
New-NetFirewallRule -DisplayName "Open Port 12345" -Direction Inbound -Protocol TCP -LocalPort 12345 -Action Allow
"
exit
