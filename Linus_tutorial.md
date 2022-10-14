#建立github SSH keys
##在/home/pi建立目錄 .ssh
cd ~

建立.shh目錄

mkdir .ssh

進入目錄

cd .ssh

建立金鑰

ssh-keygen

使用vim copy金鑰內容，並貼上至gitHub內

vim id_rsa.pub