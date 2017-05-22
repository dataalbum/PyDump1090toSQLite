https://ferrancasanovas.wordpress.com/2013/09/26/dump1090-installation/

Error opening the RTLSDR device: Device or resource busy
FiX
git clone git://git.osmocom.org/rtl-sdr.git
cd rtl-sdr
mkdir build
cd build
cmake ../ -DDETACH_KERNEL_DRIVER=ON -DINSTALL_UDEV_RULES=ON
make
sudo make install
sudo ldconfig
cd ~
sudo cp ./rtl-sdr/rtl-sdr.rules /etc/udev/rules.d/
sudo reboot

Start dump1090:
./dump1090 --interactive --net

Dump to file:
"nc 127.0.0.1 30003 | egrep --line-buffered 'MSG,3,|MSG,4,' >> logfile.csv"

Create table:
sqlite3 adsb_messages;
create table adsb_messages(timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, msg TEXT, hex TEXT, sqwk TEXT, flight TEXT, alt TEXT, lat TEXT, lon TEXT, date TEXT, time TEXT);
