# code-projects

### Concentric Shapes
#### Purpose
This program produces images of concentric shapes (circle, square, equilateral triangle) in grayscale where the intensity at some 'radius' from the center is based on a given sinusoidal function. Images are normalized according to a given contrast %. Bit size can be specified (8-bit, 16-bit, etc.) and this is handled by the `png` module.

#### Original Use
I wrote this program for use in a Psychology class experiment where participants would be asked to identify the shape of very low contrast pictures based on different sinusoidal sums. The coding itself was not required for class and I also modified the code to be more general.

#### Potential Uses
The program defines 'radius' from a center point for squares and equilateral triangles such that outputs may be drawn as a function of this radius. This does not need to be based on a sinusoid and can be modified as is desirable. The program also demonstrates how to use the `png` module to output a 16-bit image. Both these functionalities caused me a good bit of annoyance so here they are should anyone find this page.
