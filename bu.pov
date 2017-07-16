#include "colors.inc"

# declare ortofotoCenter = <722070, 0, 4669465>;
# declare YScaleHeightField = 4000; // metros de altura que corresponden al máximo en un height_field. Cuanto más alto más se exagerarán las alturas. Si el height field se ha generado asignando el valor máximo a p.ej. 4000 m. de altura, este valor debería estar en las cercanías de 4000 para el máximo realismo, pero es posible que quede mejor que sea un poco más grande.
# declare mdtPos = <704400, 0, 4652400>; // xllcenter yllcenter tal cual están en el ASC
# declare ortoLowLeft = <718450.25, 0, 4666940.25>; // coordenada inferior izquierda del JPG, ojo, no son los valores directos del JGW
# declare orto2LowLeft = <718600.25, 0, 4662309.75>; // coordenada inferior izquierda del JPG, ojo, no son los valores directos del JGW

camera { 
	orthographic
	location <732070.0, 11200, 4669465.0>
	right <5050, 0, 0>
	up <0.0, 3620, 3620>
	look_at  <722070, 1200, 4669465>
}

light_source {ortofotoCenter + <5000, 8000, 0> color White }

height_field{
	png "./PNG/MDT05-0286-H30-LIDAR.png"
	smooth // por defecto es off, pero mejora el aspecto final (aunque tarda más el render)
	// Importante: escalar el height field antes de la textura, sino estaríamos escalando la textura dos veces
	scale < 5761*5, YScaleHeightField, 4001*5 > // ancho, Y, alto del MDT en metros
	translate  mdtPos + <-2.5, 0, -2.5> // xll, yll center menos media celda (queremos la esquina)

	// ORTOFOTO 1
	texture{
		pigment { 
			//White
			image_map {
				jpeg "./PNOA/pnoa_2012_286_3_1.jpg"
				once // No queremos que se repita
			}
		}
		// estas transformaciones afectan solo a la textura, no al height_field
		scale <14480*0.5, 10100*0.5, 1>
		rotate x*90 // poner sobre XZ para que encaje con el height field
		translate ortoLowLeft + <-0.5,0,-0.5>
	}

	finish {
          ambient 0.2         // Sombras muy oscuras
          diffuse 0.8         // Blancos más brillantes
          roughness 0.05
   }
}