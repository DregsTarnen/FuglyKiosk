# FuglyKiosk

This should work fairly well with any headless Linux install. The scripts in this project will work with any kernel. The install commands you have to use will
depend on the Linux type you use. I am using Rocky Linux. So I will be using DNF and or Yum. So begin by creating a headless installation and then:

# Additional Packages

    dnf check-update
    dnf update
    dnf install tar nano wget curl net-tools lsof bash-completion Xorg urw-fonts liberation-fonts xterm tigervnc*
    dnf install tk gc gcc-c++ make python3-tkinter
    dnf install epel-release
    dnf install xdotool
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
    dnf localinstall google-chrome-stable_current_x86_64.rpm
    wget https://www.nongnu.org/xbindkeys/xbindkeys-1.8.7.tar.gz
    tar xzvf xbindkeys-1.8.7.tar.gz
    cd xbindkeys-1.8.7
    ./configure --disable-guile
    make
    make install
    
# Make A Home For Kiosk Scripts
Make a directory named fuglykiosk in your home directory and place all the fuglykiosk files in it.
You also could leave your home directory the way it is, probably has your current users folder in it.
Change the file paths in the scripts from fuglykiosk to your user directory and place files in your user directory.
    
