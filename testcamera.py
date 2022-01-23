"""how to take a single image using the AndorEmccd class"""
import time
#from andorEmccd import AndorEmccd
#cam = AndorEmccd()

import andorEmccd
from time import sleep
import matplotlib.pyplot as plt

cam = andorEmccd.AndorEmccd()

cam.set_trigger_mode(1)
#print(cam.get_temperature())
cam.set_temperature(20)
cam.set_shutter_open(True)
cam.set_exposure_time(0.1)
cam.start_acquisition(single=True)
cam.set_em_gain(10)
sleep(1)
im = cam.wait_for_image()
print(im)
plt.imshow(im)
#plt.imsave()
cam.set_shutter_open(False)
plt.show()
cam.close()


#
# im = cam.wait_for_image()
# print(im)