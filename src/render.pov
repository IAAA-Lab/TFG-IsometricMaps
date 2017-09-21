#include "colors.inc"
camera {orthographic location <721930.0, 11200, 4664095.0> right <7240, 0, 0> up <0.0, 2524.9999999999995, 2525.0> look_at <721930.0, 1200, 4674095.0>}
light_source {<721930.0, 0, 4674095.0> + <5000, 8000, 0> color White }
height_field {png "../PNG/MDT05-0248-H30-LIDAR.png" smooth scale <5721*5, 4000, 4001*5> translate <704000, 0, 4671000> + <-2.5, 0, -2.5>
texture{pigment{image_map{jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_3_4.jpg/pnoa_2012_248_3_4.jpg" once}} scale <7240, 5050, 1> rotate x*90 
translate <718310.0, 0, 4671570.0> + <-0.25, 0, -0.25>}
finish { ambient 0.2 diffuse 0.8 roughness 0.05 }}