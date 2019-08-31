from __future__ import print_function
import os, sys, time

# GOOGLE API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

# DB credentials
db_credentials = ""

# openCV 적용 파일 이름
file_name = 'temp.jpg'

sys.path.append('lib/')
from BlurPlot_TEST import BlurPlot
from googleOCR import detect_document, detect_text
from searchDB import searchDB


if __name__ == "__main__":
    # process multiple images
    images = ['samples/'+f for f in os.listdir('samples/')]

    f = open('output.txt', 'w+')

    for image in images:
        BlurPlot(image)

        text = detect_text(file_name)

        if len(text) > 2:
            if len(text[1]) < 12: res = text[1] + text[2]
        else: res = text[1]

        if len(res) > 17:
            # 예외처리 letters
            if res[0] in '4ABFKMNRWXYZabfkmnrwxyz*%#Ж': res = res[1:]
            if len(res) > 17:
                if res[-1] in '4ABKFMNRWXYZabfkmnrwxyz*%#Ж': res = res[:-1]

        f.write(res + '\n')

        print(res)

        time.sleep(1)

    f.close()