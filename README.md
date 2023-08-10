# Low-Poly_Generator

Summary: 
This project takes an image (JPG or PNG) and recreates the image with a series of trinagles. This is achieved through image processesing, starting with line detection. Using the OpenCV library, the program detects edges using a gaussian blur. Then, the program uses delauny triangulation on randomly selected points that lie on the edges. Finally, the program takes the average RGB color value of the corners of each triangle and makes that the color of the triangles. The size of the image and threshhold values for edge detection are adjusted in the code, along with the source image. 

Potential Future Improvements: 
A UI to adgust threshold values, number of nodes, and size. 

Use: 
This project was used to create art for a Graphic Design class I took, along with background art for various other projects, including the banner for my portfolio. 

Resources:
https://homepages.inf.ed.ac.uk/rbf/HIPR2/linedet.htm
https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html 
