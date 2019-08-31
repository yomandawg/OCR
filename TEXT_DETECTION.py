from __future__ import print_function
import os, sys

# GOOGLE API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

# DB credentials
db_credentials = ""

# openCV 적용 파일 이름
file_name = 'temp.jpg'

sys.path.append('lib/')
from BlurPlot import BlurPlot
from googleOCR import detect_document, detect_text
from searchDB import searchDB


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('파일명을 확인해주세요')
        exit()

    BlurPlot(f'{sys.argv[1]}')

    # GOOGLE API detect_text
    text = detect_text(file_name)
    res = text[1]

    # GOOGLE API detect_docuemnt
    # document = detect_document(file_name)
    # res = max(document, key=lambda x: x[1])[0]
    
    # 예외처리 letters
    if len(res) > 17:
        if res[0] in '4ABKFMNRWXYZabfkmnrwxyz*%#Ж': res = res[1:]
        if len(res) > 17:
            if res[-1] in '4ABKFMNRWXYZabfkmnrwxyz*%#Ж': res = res[:-1]

    print(res)

    # Search the DB for corresponding data
    # if len(res) == 17: searchDB(res, db_credentials)