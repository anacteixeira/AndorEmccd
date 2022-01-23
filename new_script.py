"""An example of how to take a single image using the AndorEmccd class"""
import time
#from andorEmccd import AndorEmccd
#cam = AndorEmccd()

import andorEmccd
from time import sleep
import matplotlib.pyplot as plt

cam = andorEmccd.AndorEmccd()

print(cam.get_temperature())
cam.set_shutter_open(True)
cam.set_exposure_time(0.1)
cam.start_acquisition(single=True)
sleep(1)
im = cam.wait_for_image()
print(im)
plt.imshow(im)
cam.set_shutter_open(False)
plt.show()
cam.close()


#
# im = cam.wait_for_image()
# print(im)