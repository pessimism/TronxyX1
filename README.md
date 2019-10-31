# TronxyX1

## Introduction

The [Tronxy X1](http://www.tronxy.com/x-series/tronxy-x1.html) is a budget cantilever design 3D printer by Tronxy.  I purchased this as my entry into the world of 3D printing.  

This repository contains documentation and resources I have collected while experimenting with this printer.

## Purchasing

All purchasing information here is focused on purchasing from Canada in Canadian Dollars (CAD).

I purchased my Tronxy X1 at [GearBest](https://www.gearbest.com/3d-printers-3d-printer-kits/pp_494192.html).  At the time of purchase, the kit was on flash sale for $133.  I was not given an option to choose shipping for this deal.  It was shipped by DHL and time from order to arrival was one week including a weekend.  There were some surprise customs fees from DHL bringing total cost to $159 to my door.  To their credit, DHL made payment of customs fees a painless online process and sent SMS status messages about the shipment and the need to pay fees.  

My first filament purchase was the [Sunlu PLA+](http://www.sunlugw.com/pd.jsp?id=52#_pp=151_1343) from [Amazon Canada](https://www.amazon.ca/gp/product/B07FXJ6PKQ/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1).  Cost for the 1KG spool was $20.39 on sale plus taxes totalling $23.04 (I have a Prime membership so did not pay extra for shipping).  The filament appears to be of good quality so far and I have not yet had any clogging or other issues caused by filament quality.

I purchased this [ten pack of roller wheels](https://www.amazon.ca/gp/product/B07CWM3GCM/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1) at a shipped cost of $1.58 each to replace one wheel shipped with the unit that was scratched causing the x-axis to catch on the rail at a certain point.  The new wheel worked but these appear to be of poor quality, do not spin effortlessly by hand and have slight surface imperfections in the plastic.  I will search for higher quality rollers later as an upgrade option.

## Folder Structure

Documentation - The factory documentation shipped with the printer

Drivers - The USB to serial interface driver required to control the printer by computer

Models - Model files for the factory demo part, useful calibration items and upgrade parts specific to the printer

Profiles - Printer and Filament configuration profiles I have built and found to work well with my particular setup.

## Bed Adhesion

I had difficulty with adhesion with the bare Garolite build plate and Sunlu PLA+.  I added a layer of inexpensive 3M green painter's tape locally purchased and had much better results.

After printing and removing several items I had adhesion issues again which were improved by wiping down the tape surface with alcohol, finger oils can make the difference between adhesion and failure.

## Firmware Calibration
I found that even after belt tensioning to the best of my ability with the provided hardware, I had to very slightly increase the X steps/mm to get true squares/circles.  I attribute this to differences in belt tension between axes

I found my extruder was underextruding and steps/mmm needed to be increased by almost 10%.  Never assume factory calibration is correct.  This can also change from one filament to the other.  I did the adjustment using [this guide](https://all3dp.com/2/extruder-calibration-6-easy-steps-2/)

## Extruder Issues
While trying to eliminate stringing and blobbing on prints I found that the bowden tube was not fully inserted into either coupler.  The end going into the hot end was also not cut flat, so I re-trimmed the end. Trimming and re-seating the tube noticeably improved print quality.