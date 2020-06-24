#!/usr/local/bin/python

# Original file from http://www.sternwolken.de/tmpup/3dprint/pressureadvance2.py

# extrusion parameters (mm)
extrusion_width   = 0.48 # typical: nozzleDiameter * 1.2 (f.e. a 0.4mm nozzle should be set to 0.48mm extrusion width in slicers)
layer_height      = 0.2 # max: 50% of your extrusion_width
filament_diameter = 1.75 # manufacturers typically sell 1.73-1.74mm filament diameter (always lower than 1.75 to prevent cloggs) tested with many brands

# print speeds (mm/s)
travel_speed      = 200
first_layer_speed =  40
slow_speed        =  20 # speed for the slow segments
fast_speed        =  60 # speed for the fast segments
cooling_fan_speed = 128 # from 0 to 255

# calibration object dimensions (mm)
layers        = 100
object_width  = 100
num_patterns  =  4
pattern_width =  5

# pressure advance gradient (s)
pressure_advance_min = 0.0
pressure_advance_max = 0.5

# center of print bed (mm)
# needed to position this print in the middle of your print bed
# If you are not sure about this: Take a look into your slicer. Normally you will see the origin (center) visualized as xyz-axis
# f.e. I have a 285x220mm bed, my printers origin is at X0, Y0 (front left corner), so the offset value you would need for X are 285/2.0 = 142.5
offset_x = 75
offset_y = 75

layer0_z = layer_height

# put your typical start.gcode here, if you use a custom start gcode via your slicing software
# Python tipp: to type in a continuous command over multiple lines you can use a backslash '\'
# general tipp: to output a 'new line' after your gcode command use '\n' which is the representation of the new line byte sequence
# in short: use '\n\' after each line of your regular start.gcode command
f=open("linear_advance.gcode","w")
f.write('; START.gcode\n M104 S200 T0 \n M109 S200 T0\n G28 ; home all axes\n T0 ; set active extruder to 0\n G92 E0.0000 ; reset extruded length \n ')
f.write('\nM83 ; relative extrusion for this python script\n')


from math import *


def extrusion_volume_to_length(volume):
    return volume / (filament_diameter * filament_diameter * 3.14159 * 0.25)

def extrusion_for_length(length):
    return extrusion_volume_to_length(length * extrusion_width * layer_height)

curr_x = offset_x
curr_y = offset_y
curr_z = layer0_z

# goto z height
f.write("G1 X%.3f Y%.3f Z%.3f E1.0 F%.0f \n" % (curr_x, curr_y, curr_z, travel_speed * 60))

def up():
    global curr_z
    curr_z += layer_height
    f.write("G1 Z%.3f \n" % curr_z)

def line(x,y,speed):
    length = sqrt(x**2 + y**2)
    global curr_x, curr_y
    curr_x += x
    curr_y += y
    if speed > 0:
        f.write("G1 X%.3f Y%.3f E%.4f F%.0f \n" % (curr_x, curr_y, extrusion_for_length(length), speed * 60))
    else:
        f.write("G1 X%.3f Y%.3f F%.0f \n" % (curr_x, curr_y, travel_speed * 60))

def goto(x,y):
    global curr_x, curr_y
    curr_x = x + offset_x
    curr_y = y + offset_y
    f.write("G1 X%.3f Y%.3f \n" %(curr_x, curr_y))

def first_layer_raft():

    f.write('; raft layer \n')

    line(-object_width/2,0,0)

    for l in range(2):
        
        for offset_i in range(5):
            offset = offset_i * extrusion_width
            line(object_width+offset,0,first_layer_speed)
            line(0,extrusion_width+offset*2,first_layer_speed)
            line(-object_width-offset*2,0,first_layer_speed)
            line(0,-extrusion_width-offset*2,first_layer_speed)
            line(offset,0,first_layer_speed)
            line(0,-extrusion_width,0)
        up()
        goto(-object_width/2,0)

    f.write('; raft layer end \n')
        
first_layer_raft()

f.write('\nM106 S{}\n'.format(cooling_fan_speed))

segment = (object_width*1.0) / num_patterns
space = segment - pattern_width

for l in range(layers):
    
    pressure_advance = (l / (layers * 1.0)) * (pressure_advance_max-pressure_advance_min) + pressure_advance_min;
    
    f.write("; layer %d, pressure advance: %.3f \n" %(l, pressure_advance))
    
    f.write("M900 K%.3f \n" % pressure_advance)
    
    for i in range(num_patterns):
        line(space/2, 0, fast_speed)
        line(pattern_width, 0, slow_speed)
        line(space/2, 0, fast_speed)
    
    line(0,extrusion_width,fast_speed)

    for i in range(num_patterns):
        line(-space/2, 0, fast_speed)
        line(-pattern_width, 0, slow_speed)
        line(-space/2, 0, fast_speed)
    
    line(0,-extrusion_width,fast_speed)
    up()

f.write('; END.gcode\n\
G91 ; relative\n \
G1 Z10 F450 ; bed clearance\n \
G90 ; absolute\n\
M106 S0 ; turn off part cooling fan\n\
M104 S0 ; turn off extruder\n\
M84 ; disable motors\n\
M300 S440 P200\n\
M300 S660 P250\n\
M300 S880 P300\n')