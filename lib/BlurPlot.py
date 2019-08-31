def BlurPlot(input_image, gamma=0.5):
    import cv2
    import matplotlib.pyplot as plt
    import numpy as np

    img = cv2.imread(input_image)

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    adjusted = cv2.LUT(img, table)

    gray = cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=40.0, tileGridSize=(8,8))

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    imgray_ad = clahe.apply(blur) # adaptive
    imgray = cv2.equalizeHist(blur) # global

    res = np.hstack((imgray, imgray_ad))

    plt.figure(figsize=(40, 40))
    plt.imshow(res, cmap='gray', aspect='equal')
    plt.axis('off')
    plt.savefig('temp.jpg', bbox_inches='tight')

    plt.close()