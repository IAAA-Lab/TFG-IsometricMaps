echo $1
echo $2.jpg
gdalwarp -s_srs EPSG:25831 -t_srs EPSG:25830 -of GTiff -dstalpha -co "TFW=YES" $1/$2.jpg/$2.jpg $1/$2.jpg/$2.tif
rm $1/$2.jpg/*.jpg $1/$2.jpg/*.jgw
mv $1/$2.jpg/*.tfw $1/$2.jpg/$2.jgw

echo $3.jpg
gdalwarp -s_srs EPSG:25831 -t_srs EPSG:25830 -of GTiff -dstalpha -co "TFW=YES" $1/$3.jpg/$3.jpg $1/$3.jpg/$3.tif
rm $1/$3.jpg/*.jpg $1/$3.jpg/*.jgw
mv $1/$3.jpg/*.tfw $1/$3.jpg/$3.jgw

echo $4.jpg
gdalwarp -s_srs EPSG:25831 -t_srs EPSG:25830 -of GTiff -dstalpha -co "TFW=YES" $1/$4.jpg/$4.jpg $1/$4.jpg/$4.tif
rm $1/$4.jpg/*.jpg $1/$4.jpg/*.jgw
mv $1/$4.jpg/*.tfw $1/$4.jpg/$4.jgw

echo $5.jpg
gdalwarp -s_srs EPSG:25831 -t_srs EPSG:25830 -of GTiff -dstalpha -co "TFW=YES" $1/$5.jpg/$5.jpg $1/$5.jpg/$5.tif
rm $1/$5.jpg/*.jpg $1/$5.jpg/*.jgw
mv $1/$5.jpg/*.tfw $1/$5.jpg/$5.jgw

echo $6.jpg
gdalwarp -s_srs EPSG:25831 -t_srs EPSG:25830 -of GTiff -dstalpha -co "TFW=YES" $1/$6.jpg/$6.jpg $1/$6.jpg/$6.tif
rm $1/$6.jpg/*.jpg $1/$6.jpg/*.jgw
mv $1/$6.jpg/*.tfw $1/$6.jpg/$6.jgw

echo $7.jpg
gdalwarp -s_srs EPSG:25831 -t_srs EPSG:25830 -of GTiff -dstalpha -co "TFW=YES" $1/$7.jpg/$7.jpg $1/$7.jpg/$7.tif
rm $1/$7.jpg/*.jpg $1/$7.jpg/*.jgw
mv $1/$7.jpg/*.tfw $1/$7.jpg/$7.jgw

echo $8.jpg
gdalwarp -s_srs EPSG:25831 -t_srs EPSG:25830 -of GTiff -dstalpha -co "TFW=YES" $1/$8.jpg/$8.jpg $1/$8.jpg/$8.tif
rm $1/$8.jpg/*.jpg $1/$8.jpg/*.jgw
mv $1/$8.jpg/*.tfw $1/$8.jpg/$8.jgw

echo $9.jpg
gdalwarp -s_srs EPSG:25831 -t_srs EPSG:25830 -of GTiff -dstalpha -co "TFW=YES" $1/$9.jpg/$9.jpg $1/$9.jpg/$9.tif
rm $1/$9.jpg/*.jpg $1/$9.jpg/*.jgw
mv $1/$9.jpg/*.tfw $1/$9.jpg/$9.jgw
