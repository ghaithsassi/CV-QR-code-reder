import cv2
import numpy as np
from pyzbar.pyzbar import decode
import requests
import imutils

#########################################
URL = "http://192.168.0.24:8080/shot.jpg"
CAMPORT = 0
heightImg = 1080
widthImg = 720
#########################################


def main():
    # cap = cv2.VideoCapture(CAMPORT, cv2.CAP_DSHOW)
    while True:
        img_resp = requests.get(URL)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        img = imutils.resize(img, width=widthImg, height=heightImg)
        success = True
        # success, img = cap.read()
        if success:
            for b_code in decode(img):
                data = b_code.data.decode("utf-8")
                print(data)

                points = np.array([b_code.polygon], np.int32)
                points = points.reshape((-1, 1, 2))

                cv2.polylines(img, [points], True, (0, 0, 255), 2)

        cv2.imshow("window", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


###########################################

if __name__ == "__main__":
    main()
