.. pyimg-process documentation master file, created by
   sphinx-quickstart on Fri Oct 28 10:07:44 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pyimg-process: The easiest tool to perform basic image processing transformations.
==================================================================================
.. toctree::
   :maxdepth: 5
   :caption: Contents: 

In this document you will find all the functionalitys of pyimg-process. This library has been designed to make easier the adaptation for begginers to image processing world, creating basic functions that a specialist on this area must know.
For easier manipulation, is recommended to instance de class in the next way::  
   
      from pyimg_process.Methods import Methods
      m = Methods()

Read Image 
----------
.. py:function:: def read_image(path, filename):

   This function is used to load images. Is necessary to specify the path and the name of the image.

   :param path: The path where is the image. It could be absolute or relative.
   :type [path: str
   :param filename: Image name.
   :type [filename: str
   :raises Error:  In case of not finding the image, it will raise an error.
   :return: It return the image array in RGB format or in grayscale format, depending the format of the image introduced.
   :rtype: array.

Write Image
-----------
.. py:function:: def write_image(filename, img, same_path=True, **kwargs):

   This function is used to write the image in the path specified. If the same_path is True, the image will be saved in the same path where the original image is. If the same_path is False, the image will be saved in the path specified in the path parameter introduced using *kwargs*.
   

   :param filename: Image name.
   :type [filename: str
   :param img: Image array.
   :type [img: array
   :param same_path: If True, the image will be saved in the same path where the original image is. If False, the image will be saved in the path specified in the path parameter introduced using *kwargs*.
   :type [same_path: bool
   :param kwargs: It will be only used in case of wanting to write the image in a different path to original image. It must be introduced as *path='path'*.
   :print: In case of writing succesfully, it will print the message `Image written in path`.

Show Image
----------
.. py:function:: def show_image(img):

   This function is used to show the image. On the one hand, in case of introducing a grayscale image, it will be shown in grayscale format. On the other hand, in case of introducing a RGB image, it will be shown in RGB format.

   :param img: Image array.
   :type [img: array
   :plot: It will show the image.

Resize Image
------------
.. py:function:: def resize(img, output_size):

   This function is used to resize the image. It is necessary to specify the output size of the image.

   :param img: Image array.
   :type [img: array
   :param output_size: New size to which we want to transform the image.
   :type [output_size: tuple
   :return: It return the image array resized.
   :rtype: array.

Grayscale Image
---------------
.. py:function:: def grayscale(img):

   This function is used to transform the image from RGB format to grayscale format.

   :param img: Image array.
   :type [img: array
   :return: It return the image array in grayscale.
   :rtype: array.

Blur Filter
-----------
.. py:function:: def blur(img, kernel_size):

   This function is used to blur the image with the aim of making less abrupt the changes of intensity in the image. It is necessary to specify the kernel size.

   :param img: Image array.
   :type [img: array
   :param kernel_size: Number of rows and columns will have the kernel matrix.
   :type [img: int
   :return: It return the image array blurred.
   :rtype: array.

Sharpen Filter
--------------
.. py:function:: def sharpen(img, kernel_size):

   This function is used to sharpen the image with the aim of highlighting the edges and details, and reducing the blur. 

   :param img: Image array.
   :type [img: array
   :param kernel_size: Number of rows and columns will have the kernel matrix.
   :type [img: int
   :return: It return the image array sharpened.
   :rtype: array.

Histogram of the Image
----------------------
.. py:function:: def histogram(img):

   This function is used to show the histogram of the image to show the distribution of image pixels values.

   :param img: Image array.
   :type [img: array
   :plot: It will show the histogram of image pixels values.

Threshold Filter
----------------
.. py:function:: def threshold(img, hist=False, **kwargs):

   This function is used to apply a threshold filter to the image. It is necessary to specify the threshold value. If the hist is True, it will show the histogram of the image to show the distribution of image pixels values.

   :param img: Image array.
   :type [img: array
   :param hist: If True, it will show the histogram of the image.
   :type [hist: bool
   :param kwargs: This will be used to specify the threshold value. It will depend if it is wanted to use only one value as thresholding or a range. If it is wanted to change al values above a specific value only one value must be introduced. In contrast, if is wanted to focus on the region of interest (ROI) of the image, it is necessary to introduce the range of values. It must be introduced as *threshold=(min, max)*.
   :type [img: int
   :return: It return the resulting image of the thresholding filter.
   :rtype: array.

Inverse Filter
--------------
.. py:function:: def inverse(img, gray=False):

   This function is used to apply an inverse filter to the image. If the gray is True, it will be applied to the grayscale image. If the gray is False, it will be applied to the RGB format image.

   :param img: Image array.
   :type [img: array
   :param gray: If True, it will be applied to the grayscale image. If False, it will be applied to the RGB format image.
   :type [hist: bool
   :return: It return the resulting image of the inverse filter.
   :rtype: array.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

