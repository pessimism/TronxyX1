$fn=100;

difference(){
    cube([20,20,20]);
    translate([1,1,2])rotate([90,0,0])linear_extrude(height=1)text("Super",size=5);
    translate([19,1,12])rotate([90,0,90])linear_extrude(height=1)text("Cube",size=5);
    translate([10,1,19])rotate([0,0,90])linear_extrude(height=1)text("20x20x20",size=3);
    translate([0,9,0])rotate([0,90,0])cylinder(d=15,h=20);
    translate([14,1,12])rotate([90,0,0])linear_extrude(height=1)text("8mm",size=2);
    translate([10,0,15])rotate([-90,0,0])cylinder(d=8,h=20);
    translate([2,0,15])cube([3,20,5]);
    translate([0,3,15])cube([2,14,5]);
    translate([17,17,0])cube([3,3,20]);
}

difference(){
    translate([17,17,0])cylinder(d=6,h=20);
    translate([0,9,0])rotate([0,90,0])cylinder(d=15,h=20);
}

