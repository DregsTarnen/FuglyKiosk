# FuglyKiosk

This should work fairly well with any headless Linux install. The scripts in this project will work with any kernel. The install commands you have to use will
depend on the Linux type you use. I am using Rocky Linux. So I will be using DNF and or Yum. So begin by creating a headless installation and then:

# Additional Packages

    dnf check-update
    dnf update
    dnf install tar nano wget curl net-tools lsof bash-completion Xorg urw-fonts liberation-fonts xterm tigervnc*
    dnf install epel-release
    dnf install xdotool
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
    dnf localinstall google-chrome-stable_current_x86_64.rpm