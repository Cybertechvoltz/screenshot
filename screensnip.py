import pyscreenshot
as py
import datetime
import time
time.sleep(3)
i,=ps.grab()
im.save("screenshot-"+str(datetime.now()) + ".png")
im.show()