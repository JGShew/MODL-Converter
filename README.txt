--MODL Converter--
A python script to convert Wavefront .obj 3D model files to a custom binary 3D model file format, .modl. I created this for a project in which I needed to make use of 3D models. Wavefront .obj files are simple, but they are in text format, rather than binary. So, I created an equally simple binary 3D model format, which I have named MODL. I did this because binary files are generally smaller in size than text format files encoding the same data, and because implementing support for a binary 3D model format will be easier than implementing support for one in text format in C++, the language in which I will be writing the project. I have uploaded the converter and the .modl file format specification (modlform.txt in this repository) in case anyone, anywhere, anytime could possibly find this useful.

The python script has been tested to be working using python 3.9. Usage of the script is as follows:
py obj2modl.py [Wavefront .obj file] [Output .modl file]
