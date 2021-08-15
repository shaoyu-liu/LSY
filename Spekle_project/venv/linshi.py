def point(img):
    dst=img.copy()
    channels=img.ndim
    h,w=img.shape[:2]
    gray_img=np.zeros((3,3), dtype=np.uint8)

    b_img=img[:,:,0]
    cv2.namedWindow("image",cv2.WINDOW_FREERATIO)
    cv2.imshow('image',b_img)
    cv2.waitKey(0)
    ret,bin_img=cv2.threshold(b_img,150,255,0)

    cv2.imshow('bin_img',bin_img)
    cv2.waitKey(0)
    contours, heridency = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    centers=[]
    min_r=5
    max_r=50

    max_area = max_r*max_r*3.1415926
    min_area = min_r*min_r*3.1415926
    for i in range(len(contours)):
        temp_area = cv2.contourArea(contours[i])
        if temp_area > min_area and temp_area < max_area:
            cv2.drawContours(dst, contours, i, (0,255,0), -1)
            moment = cv2.moments(contours[i], True)
            center_point = (int(moment['m10'] / moment['m00']), int(moment['m01'] / moment['m00']))
            centers.append(center_point)
            cv2.line(dst, (center_point[0] - 15, center_point[1]), (center_point[0] + 15, center_point[1]),
                             (255, 0, 0), 5)
            cv2.line(dst, (center_point[0], center_point[1] - 15), (center_point[0], center_point[1] + 15),
                             (255, 0, 0), 5)
            return center_point

