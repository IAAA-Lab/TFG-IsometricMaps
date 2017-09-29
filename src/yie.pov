#include "colors.inc"

camera {
	orthographic 
	location <708165.0, 11200, 4663670.0> 
	right <7230, 0, 0> 
	up <0.0, 2519.9999999999995, 2520.0> 
	look_at <708165.0, 1200, 4673670.0>
}

light_source {<708165.0, 0, 4673670.0> + <5000, 8000, 0> color White }

height_field {

	png "../PNG/MDT05-0248-H30-LIDAR.png"
	smooth
	scale <5721*5, 4000, 4001*5>
	translate <704000, 0, 4671000> + <-2.5, 0, -2.5>

	texture{
		pigment{
			image_map{
				jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_1_3.jpg/pnoa_2012_248_1_3.jpg"
				once
			}
		}
		scale <7230.0, 5040.0, 1>
		rotate x*90
		translate <704410.0, 0, 4675779.5> + <-0.25, 0, -0.25>
	}

	texture{
		pigment{
			image_map{
				jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_1_4.jpg/pnoa_2012_248_1_4.jpg"
				once
			}
		}
		scale <7230.0, 5040.0, 1>
		rotate x*90
		translate <704550.0, 0, 4671149.5> + <-0.25, 0, -0.25>
	}
	
	finish { 
		ambient 0.2 
		diffuse 0.8 
		roughness 0.05
	}
}

