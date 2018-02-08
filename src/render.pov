#include "colors.inc"

camera {
orthographic
location <774363.248046875, 11200, 4720635.826171875>
right <2304.94921875, 0, 0>
up <0.0, 1152.4746093749998, 1152.474609375>
look_at <774363.248046875, 1200, 4730635.826171875>}

light_source {<800000, 8000000, 4900000> color White parallel}

height_field {
png "/media/pablo/280F8D1D0A5B8545/TFG_files/PNG/PNOA_MDT05_ETRS89_HU30_0179_LID.png"
smooth
scale <5639*5, 4000, 3939*5>
translate <757750, 0, 4710040> + <-2.5, 0, -2.5>
texture {
pigment {
image_map {
png "/media/pablo/280F8D1D0A5B8545/TFG_files/PNOA/PNOA_MDT05_ETRS89_HU30_0147_LID/pnoa_2015_25831_0147_3_4.jpg/pnoa_2015_25831_0147_3_4.png"
once}}
scale <7533.1428259628, 5549.446892906, 1>
rotate x*90
translate <771019.1882135238, 0, 4728791.942217562>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
texture {
pigment {
image_map {
png "/media/pablo/280F8D1D0A5B8545/TFG_files/PNOA/PNOA_MDT05_ETRS89_HU30_0179_LID/pnoa_2015_25831_0179_3_1.jpg/pnoa_2015_25831_0179_3_1.png"
once}}
scale <7522.642667872, 5548.4491432649, 1>
rotate x*90
translate <771207.5171165059, 0, 4724172.129088386>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
}
height_field {
png "/media/pablo/280F8D1D0A5B8545/TFG_files/PNG/PNOA_MDT05_ETRS89_HU30_0147_LID.png"
smooth
scale <5625*5, 4000, 3939*5>
translate <757060, 0, 4728540> + <-2.5, 0, -2.5>
texture {
pigment {
image_map {
png "/media/pablo/280F8D1D0A5B8545/TFG_files/PNOA/PNOA_MDT05_ETRS89_HU30_0147_LID/pnoa_2015_25831_0147_3_4.jpg/pnoa_2015_25831_0147_3_4.png"
once}}
scale <7533.1428259628, 5549.446892906, 1>
rotate x*90
translate <771019.1882135238, 0, 4728791.942217562>
finish {
ambient 0.2
diffuse 0.8
roughness 0.05
}
}
}
