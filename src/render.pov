#include "colors.inc"

camera {
orthographic
location <726000.0, 11200, 4664000.0>
right <10000.0, 0, 0>
up <0.0, 3999.999999999999, 4000.0>
look_at <726000.0, 1200, 4674000.0>}

light_source {<800000, 8000000, 4900000> color White parallel}

height_field {
png "../PNG/MDT05-0248-H30-LIDAR.png"
smooth
scale <5721*5, 4000, 4001*5>
translate <704000, 0, 4671000> + <-2.5, 0, -2.5>
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_3_3.jpg/pnoa_2012_248_3_3.jpg"
once}}
scale <7240.0, 5060.0, 1>
rotate x*90
translate <718160.0, 0, 4676189.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_4_3.jpg/pnoa_2012_248_4_3.jpg"
once}}
scale <7240.0, 5060.0, 1>
rotate x*90
translate <725040.0, 0, 4676409.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_3_4.jpg/pnoa_2012_248_3_4.jpg"
once}}
scale <7240.0, 5050.0, 1>
rotate x*90
translate <718310.0, 0, 4671569.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_4_4.jpg/pnoa_2012_248_4_4.jpg"
once}}
scale <7240.0, 5060.0, 1>
rotate x*90
translate <725190.0, 0, 4671779.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
}
height_field {
png "../PNG/MDT05-0286-H30-LIDAR.png"
smooth
scale <5761*5, 4000, 4001*5>
translate <704400, 0, 4652400> + <-2.5, 0, -2.5>
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0286-H30-LIDAR/pnoa_2012_286_3_1.jpg/pnoa_2012_286_3_1.jpg"
once}}
scale <7240.0, 5050.0, 1>
rotate x*90
translate <718450.0, 0, 4666939.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0286-H30-LIDAR/pnoa_2012_286_4_1.jpg/pnoa_2012_286_4_1.jpg"
once}}
scale <7240.0, 5060.0, 1>
rotate x*90
translate <725340.0, 0, 4667159.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
}
