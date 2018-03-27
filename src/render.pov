#include "colors.inc"

camera {
orthographic
location <649895.990234375, 11200, 4533190.396484375>
right <2304.94921875, 0, 0>
up <0.0, 1152.4746093749998, 1152.474609375>
look_at <649895.990234375, 1200, 4523190.396484375>}

light_source {<800000, 8000000, 4900000> color White parallel}

height_field {
png "/media/pablo/280F8D1D0A5B8545/TFG_files/PNG/PNOA_MDT05_ETRS89_HU30_0516_LID.png"
smooth
scale <5721*5, 4000, 3829*5>
translate <624660, 0, 4502750> + <-2.5, 0, -2.5>
texture {
pigment {
image_map {
jpeg "/media/pablo/280F8D1D0A5B8545/TFG_files/PNOA/PNOA_MDT05_ETRS89_HU30_0491_LID/pnoa_2015_25830_0491_4_4.jpg/pnoa_2015_25830_0491_4_4.jpg"
once}}
scale <7330.0, 4980.0, 1>
rotate x*90
translate <645600.0, 0, 4521589.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
texture {
pigment {
image_map {
jpeg "/media/pablo/280F8D1D0A5B8545/TFG_files/PNOA/PNOA_MDT05_ETRS89_HU30_0516_LID/pnoa_2015_25830_0516_4_1.jpg/pnoa_2015_25830_0516_4_1.jpg"
once}}
scale <7330.0, 4980.0, 1>
rotate x*90
translate <645690.0, 0, 4516959.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
}
height_field {
png "/media/pablo/280F8D1D0A5B8545/TFG_files/PNG/PNOA_MDT05_ETRS89_HU30_0491_LID.png"
smooth
scale <5707*5, 4000, 3829*5>
translate <624350, 0, 4521250> + <-2.5, 0, -2.5>
texture {
pigment {
image_map {
jpeg "/media/pablo/280F8D1D0A5B8545/TFG_files/PNOA/PNOA_MDT05_ETRS89_HU30_0491_LID/pnoa_2015_25830_0491_4_3.jpg/pnoa_2015_25830_0491_4_3.jpg"
once}}
scale <7320.0, 4970.0, 1>
rotate x*90
translate <645510.0, 0, 4526219.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
texture {
pigment {
image_map {
jpeg "/media/pablo/280F8D1D0A5B8545/TFG_files/PNOA/PNOA_MDT05_ETRS89_HU30_0491_LID/pnoa_2015_25830_0491_4_4.jpg/pnoa_2015_25830_0491_4_4.jpg"
once}}
scale <7330.0, 4980.0, 1>
rotate x*90
translate <645600.0, 0, 4521589.5>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
}
