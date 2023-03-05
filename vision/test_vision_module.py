from vision import Vision
from compute_pose import ComputePose
import threading

V = Vision()
C = ComputePose(V)

threading.Thread(target=V._detect_object).start()
C._callibrate()
