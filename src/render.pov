#include "colors.inc"

camera {
orthographic
location <818157.283203125, 11200, 4607693.314453125>
right <2304.94921875, 0, 0>
up <0.0, 1152.4746093749998, 1152.474609375>
look_at <818157.283203125, 1200, 4617693.314453125>}

light_source {<800000, 8000000, 4900000> color White parallel}

height_field {
png "/media/pablo/280F8D1D0A5B8545/TFG_files/PNG/PNOA_MDT05_ETRS89_HU30_0359_LID.png"
smooth
scale <5725*5, 4000, 3961*5>
translate <788850, 0, 4618560> + <-2.5, 0, -2.5>
}
