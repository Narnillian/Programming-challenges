# #243 -- Polygons
Calculate degree measurements of angles of Regular Polygons

## About
Started Monday, April 11, the second day of the challenge. The challenge was to calculate the interior angle measurement of a polygon with the given number of sides. I added some extra functionality. My version calculates not only the measure of each interior angle measurement, but also the interior angle sum, the size of a single exterior angle (the sum of exterior angles is always 360), and the number of diagonals in the polygon.

<br>

## Usage
`regular_polygons [args] <number_of_sides>`

Example:

`regular_polygons ias diags 78`

Optional arguments:

`ias` -- Calculate **I**nterior **A**ngle **S**um (sum of all interior angles)

`iam` -- Calculate **I**nterior **A**ngle **M**easure (size of one interior angle)

`eam` -- Calculate **E**xternal **A**ngle **M**easure (size of one exterior angle)

`diags` -- Calculate number of **Diag**onal**s** in the polygon

***You must specify a number of sides***
