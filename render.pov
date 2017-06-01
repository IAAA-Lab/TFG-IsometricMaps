#include "colors.inc"
 
camera{
    location <0, 2, -10>
    look_at 0
    angle 30
}

light_source{ <1000,1000,-1000> White }

object
{
	height_field{
		png "./PNG/MDT05-0248-H30-LIDAR.png"
		smooth
	}
	pigment { White }
	scale <17,1.75,17>
	translate <-.5,-.5,-.5>
}