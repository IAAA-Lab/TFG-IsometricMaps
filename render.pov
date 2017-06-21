#include "colors.inc"

camera { 
	orthographic angle 50
    location <15, 15, -15>
    look_at  <0, 0, 0>
    right x * image_width / image_height
    translate <0, 2.00, 0>
}

global_settings {ambient_light rgb <1.00000, 1.0000, 1.0000> }
light_source { <2000, 2000, 0> White parallel point_at <0,0,0> fade_power 0 }

object
{
	height_field{
		png 
		"./PNG/MDT05-0286-H30-LIDAR-D/MDT05-0286-H30-LIDAR_2.png"
		hierarchy on
		texture{
			pigment { 
				image_map {
					jpeg "./PNOA/pnoa_2012_286_3_1.jpg"
				}
				scale 0.5
			}
		}
	}

	scale <20,10,20>
	translate <-1, 2,-20>
}	  