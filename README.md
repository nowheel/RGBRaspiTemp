# RGBRaspiTemp

Script for check in 1 second the temperature of your Raspi, Simple! you look the single rgb led and the color show temperature. 
created for using with octopus, but you can use everywhere.

Note: make sure of the schema you want to build for the led, potentially you can use the led strip, but if you don't use external power,
you can burn the raspi. 

There is various video on youtube where explain the schema to build for stripes if you want to try.

-------------------------------------------------------------
 HOW TO:

  make executable:
  
     $:chmod +x led.py

  add to crontab with :
  
     $:crontab -e

  In editor add to last line:  !! Change /___folder_where_/your_put_the_file___/ with the folder
                                  where you put the led.py file. !!!

     @reboot sudo python /___folder_where_/your_put_the_file___/led.py       

