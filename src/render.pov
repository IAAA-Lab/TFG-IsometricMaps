#include "colors.inc"
camera {orthographic location <722220.0, 11200, 4654840.0> right <7240, 0, 0> up <0.0, 2529.9999999999995, 2530.0> look_at <722220.0, 1200, 4664840.0>}
light_source {<722220.0, 0, 4664840.0> + <5000, 8000, 0> color White }
height_field {png "../PNG/MDT05-0286-H30-LIDAR.png" smooth scale <5761*5, 4000, 4001*5> translate <704400, 0, 4652400> + <-2.5, 0, -2.5>
texture{pigment{image_map{jpeg "../PNOA/pnoa_2012_286_3_2.jpg/pnoa_2012_286_3_2.jpg" once}} scale <7240, 5060, 1> rotate x*90 translate <718600.0, 0, 4662310.0> + <-0.25, 0, -0.25>}
finish { ambient 0.2 diffuse 0.8 roughness 0.05 }}