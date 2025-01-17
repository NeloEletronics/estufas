# estufas

Instruções para o SHT30

executar o raspi-config para activar as ports I2C

instalar a bibliotecas: 
sudo pip3 install flash-restful
sudo pip3 install adafruit-circuitpython-sht31d

Activar serviço
cp estufas/service/temperature.service /lib/systemd/system
sudo systemctl daemon-reload ???
sudo systemctl enable temperature.service

## Watchdog
crontab -e
* * * * * /home/pi/estufas/check_temperature_service.sh
