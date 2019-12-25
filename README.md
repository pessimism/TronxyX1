# TronxyX1

## Introduction

The [Tronxy X1](http://www.tronxy.com/x-series/tronxy-x1.html) is a budget cantilever design 3D printer by Tronxy.  I purchased this as my entry into the world of 3D printing.  

This repository contains documentation and resources I have collected while experimenting with this printer.

## Purchasing

All purchasing information here is focused on purchasing from Canada in Canadian Dollars (CAD).

I purchased my Tronxy X1 at [GearBest](https://www.gearbest.com/3d-printers-3d-printer-kits/pp_494192.html).  At the time of purchase, the kit was on flash sale for $133.  I was not given an option to choose shipping for this deal.  It was shipped by DHL and time from order to arrival was one week including a weekend.  There were some surprise customs fees from DHL bringing total cost to $159 to my door.  To their credit, DHL made payment of customs fees a painless online process and sent SMS status messages about the shipment and the need to pay fees.  

My first filament purchase was the [Sunlu PLA+](http://www.sunlugw.com/pd.jsp?id=52#_pp=151_1343) from [Amazon Canada](https://www.amazon.ca/gp/product/B07FXJ6PKQ/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1).  Cost for the 1KG spool was $20.39 on sale plus taxes totalling $23.04 (I have a Prime membership so did not pay extra for shipping).  The filament appears to be of good quality so far and I have not yet had any clogging or other issues caused by filament quality.

[CCTREE PLA](https://www.amazon.ca/CCTREE-1-75mm-PLA-Printer-Filament/dp/B07737W8Y9) So far seems to print at a lower temperature with fewer stringing/blobbing issues than the Sunlu.

I purchased this [ten pack of roller wheels](https://www.amazon.ca/gp/product/B07CWM3GCM/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1) at a shipped cost of $1.58 each to replace one wheel shipped with the unit that was scratched causing the x-axis to catch on the rail at a certain point.  The new wheel worked but these appear to be of poor quality, do not spin effortlessly by hand and have slight surface imperfections in the plastic.  I will search for higher quality rollers later as an upgrade option.

## Folder Structure

Documentation - The factory documentation shipped with the printer

Drivers - The USB to serial interface driver required to control the printer by computer

Models - Model files for the factory demo part, useful calibration items and upgrade parts specific to the printer

Profiles - Printer and Filament configuration profiles I have built and found to work well with my particular setup.

Marlin 2.0 Config - Configuration files to build Marlin 2.0 firmware for the printer

## Bed Adhesion

I had difficulty with adhesion with the bare Garolite build plate and Sunlu PLA+.  I added a layer of inexpensive 3M green painter's tape locally purchased and had much better results.

After printing and removing several items I had adhesion issues again which were improved by wiping down the tape surface with alcohol, finger oils can make the difference between adhesion and failure.

After more printing I've abandoned the tape for now and lightly sanded the Garolite with sandpaper, cleaned with alcohol and use a layer of cheap glue stick that I wash off and reapply every few prints.  I find this faster and simpler than dealing with the tape, which I have found in some instances can actually be lifted off the Garolite by a warping print.

## Firmware Calibration
I found that even after belt tensioning to the best of my ability with the provided hardware, I had to very slightly increase the X steps/mm to get true squares/circles.  I attribute this to differences in belt tension between axes

I found my extruder was underextruding and steps/mmm needed to be increased by almost 10%.  Never assume factory calibration is correct.  This can also change from one filament to the other.  I did the adjustment using [this guide](https://all3dp.com/2/extruder-calibration-6-easy-steps-2/)

## Extruder Issues
While trying to eliminate stringing and blobbing on prints I found that the bowden tube was not fully inserted into either coupler.  The end going into the hot end was also not cut flat, so I re-trimmed the end. Trimming and re-seating the tube noticeably improved print quality.

## Marlin 2.0
I opted to upgrade the printer to Marlin 2.0 from the stock Repetier 0.91 firmware.  This gave me thermal runaway protection, a serious omission from the printer.  I was also able to add several features from much more expensive units such as print pausing and resume from power failure.  This process requires several parts to be purchased as the stock Melzi board does not ship with a bootloader installed so it can't be flashed by USB.  The way I completed the process requires:

[An Arduino UNO or compatible board](https://www.amazon.ca/gp/product/B01MTMDT29/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1) ~$15

[Female to Female AND Female to Male Dupont Jumper Wires](https://www.amazon.ca/gp/product/B01EV70C78/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) ~$12

A computer with the [Arduino IDE](https://www.arduino.cc/en/Main/Software) installed

A copy of the [Marlin 2.0 Source Code](http://marlinfw.org/meta/download/)

I will not detail all steps here as there are several good guides available online to outline the process.  I found [this one](https://www.instructables.com/id/Flashing-a-Bootloader-to-the-CR-10/) to be the most accurate.  In a nutshell you must

+ Program the UNO device via USB to act as a flashing tool 
+ Wire the UNO device to the Melzi board using six jumper wires
+ Flash a bootloader to the Melzi board via PC USB -> UNO -> Melzi connection
+ Disconnect UNO board
+ Build Marlin 2.0 using the correct Configuration.h file and any further adjustments to the Configuration_adv.h file
+ Flash Marlin to the Melzi board via PC USB

I had to make a few adjustments to the stock example Configuration and Configuration_adv files for the Tronxy X1:

+ The bed offsets were incorrect so prints were not centered in the print area
+ The thermal runaway protection was too aggressive for my room temperature and heater calibration and would error before heating was complete.  I relaxed the values as described in the documentation
+ I added my PID heater calibration values to replace the firmware defaults and made sure PID temperature control was enabled.  Further information [here](https://reprap.org/wiki/PID_Tuning)
+ I've noticed some inconsistencies in the keys required to activate menu items.  Some use left/right, some use up to confirm.  Have not resolved that yet, but all functions do work.

## Belt idler upgrade to tensioners
I purchased these [2020 extrusion compatible belt tensioners](https://www.aliexpress.com/item/4000056015276.html?spm=a2g0s.9042311.0.0.2c824c4djNLGq6) ~$15 to replace the stock single sided acrylic brackets and smoothe idler bearings.  This was the single largest upgrade in print quality I have done.  They are far better quality than the stock hardware, have toothed idlers to better fit the belt, and made a large improvement in the printer's ability to make accurate circles.  This was noticable right away in the stock demo pillar file included with the printer.

## Part Cooling Fan
I printed [this](https://www.thingiverse.com/thing:2699842) and added a 5015 fan using spare mounting nuts and screws included with the printer.  There is an open fan header on the Melzi board for this purpose.  To get proper alignment I had to rotate the heat block slightly and tweak the fan mount/shroud a little.  I have found the fan helps to prevent distortion and stringing on small posts, but it also causes the base of parts to curl up off the bed, so it is only useful in specific circumstances.