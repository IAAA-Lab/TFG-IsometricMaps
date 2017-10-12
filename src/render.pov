#include "colors.inc"

camera {
orthographic
location <717000.0, 11200, 4670000.0>
right <8000.0, 0, 0>
up <0.0, 1999.9999999999995, 2000.0>
look_at <717000.0, 1200, 4680000.0>}

light_source {<800000, 4900000, 0> color White }

height_field {
png "../PNG/MDT05-0248-H30-LIDAR.png"
smooth
scale <5721*5, 4000, 4001*5>
translate <704000, 0, 4671000> + <-2.5, 0, -2.5>
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_3_3.jpg/H_pnoa_2012_248_3_3.jpg"
once}}
scale <7240.0, 5060.0, 1>
rotate x*90
translate <718160.0, 0, 4676189.5> + <-0.25, 0, -0.25>}
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_2_3.jpg/H_pnoa_2012_248_2_3.jpg"
once}}
scale <7230.0, 5050.0, 1>
rotate x*90
translate <711290.0, 0, 4675979.5> + <-0.25, 0, -0.25>}
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_3_2.jpg/H_pnoa_2012_248_3_2.jpg"
once}}
scale <7230.0, 5050.0, 1>
rotate x*90
translate <718020.0, 0, 4680819.5> + <-0.25, 0, -0.25>}
texture {
pigment {
image_map {
jpeg "../PNOA/MDT05-0248-H30-LIDAR/pnoa_2012_248_2_2.jpg/H_pnoa_2012_248_2_2.jpg"
once}}
scale <7220.0, 5050.0, 1>
rotate x*90
translate <711150.0, 0, 4680609.5> + <-0.25, 0, -0.25>}
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
