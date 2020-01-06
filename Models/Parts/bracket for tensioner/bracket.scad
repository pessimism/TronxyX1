//To replace one side of this tensioner https://www.aliexpress.com/item/4000056015276.html
//and make it more like this one https://www.aliexpress.com/item/32993306070.html
//so that the Y carriage roller can travel the full length of the extrusion without hitting the bracket

//All dimensions in MM

//Fudge factor for hole sizes to accomodate printer/filament tolerance
fudge = 0.4;

//Dimensions for bracket
length = 74;
height = 40;
thickness = 4;

//Dimensions for notch to allow v-wheel to clear
nlength = 30; 
nheight = 20;

//Pulley slot dimensions
pheight     = 9.2 + fudge;
prad        = pheight/2;
pfromleft   = 7.3;
pfromtop    = 5.3;
pslotlength = 28.7;

//Tensioner screw holes (M3)
tensioner_screw_hole_diameter              = 3 + fudge;
tensioner_screw_hole_center_dist_from_edge = 3.5;

//T-Nut screw holes (M4)
tnut_screw_hole_diameter     = 4 + fudge;
right_tnut_offset_from_right = 8;
left_tnut_offset_from_right  = 22;

//Facet constant for hole roundness
facets = 40;

//Constant for 10mm centering of T-Nut screw holes for 2020 extrusion
2020_tnut_height = 10;

//The bracket with the notch subtracted from it
difference()
{
    //Main bracket shape
    cube([length,height,thickness], center = false);
    
    //Move notch to correct place
    translate([(length-nlength),(height-nheight),0]){
        //Notch shape
        cube([nlength,nheight,thickness], center = false);
    }
    
    //Move left pulley hole to correct place
    translate([(prad + pfromleft),(height-pfromtop-prad),0]){
        //left pulley hole
        cylinder(h = thickness, d = pheight , center = false, $fn=facets);
    }
    
    //Move right pulley hole to correct place
    translate([(prad + pslotlength),(height-pfromtop-prad),0]){
        //right pulley hole
        cylinder(h = thickness, d = pheight , center = false, $fn=facets);
    }
    
    //Move pulley rectangle to correct place
    translate([(prad + pfromleft),(height-pfromtop-pheight),0]){
        //pulley rectangle between pulley holes
        cube([(pslotlength-pheight+pfromleft-prad),pheight,thickness], center = false);
    }
    
    //Move upper tensioner screw hole to correct place
    translate([(tensioner_screw_hole_center_dist_from_edge),(height-tensioner_screw_hole_center_dist_from_edge),0]){
        //upper tensioner screw hole
        cylinder(h = thickness, d = tensioner_screw_hole_diameter , center = false, $fn=facets);
    }
    
    //Move lower tensioner screw hole to correct place
    translate([(tensioner_screw_hole_center_dist_from_edge),(height/2 + tensioner_screw_hole_center_dist_from_edge),0]){
        //lower tensioner screw hole
        cylinder(h = thickness, d = tensioner_screw_hole_diameter , center = false, $fn=facets);
    }
    
    //Move right tnut screw hole to correct place
    translate([(length - right_tnut_offset_from_right),2020_tnut_height,0]){
        //right tnut screw hole
        cylinder(h = thickness, d = tnut_screw_hole_diameter , center = false, $fn=facets);
    }
    
    //Move left tnut screw hole to correct place
    translate([(length - left_tnut_offset_from_right),2020_tnut_height,0]){
        //left tnut screw hole
        cylinder(h = thickness, d = tnut_screw_hole_diameter , center = false, $fn=facets);
    }    
}