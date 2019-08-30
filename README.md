# Histology_Patch_Extractor
Helps extract relevant patches from bigger images for model building

## Usage
python execute_patch_extractor.py -Name of bigger Image- -Full path of desired output folder- -Patch Size in pixels-
### Example
python execute_patch_extractor.py test.png /home/users/arunima2/images/output 75

### NOTE!
(1) The location file needs to be of JSON format, named the same as the image file and should be located in the same directory

Input bigger source image = test.png

Json file that is in the same directory as test.png = test.json

(2) The Json format needs to be similar to the test.json uploaded. Labels can be changed as appropriate. The x and y are centroid of locations that need to be extracted in the patches. They are depicted as ratios of width and height respectively.

x= 0.5

y= 0.7

Image_width = 700

Image_height = 900

Patch centroid = (900* 0.7, 700 * 0.5)


## Requirements
OpenCV

Python 2.7

Numpy

## Example data sourced from

https://bmcresnotes.biomedcentral.com/articles/10.1186/s13104-019-4121-7



  
