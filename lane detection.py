import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lines(img, lines):
    line_img = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 5)
    combined = cv2.addWeighted(img, 0.8, line_img, 1, 1)
    return combined

def detect_lanes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    height, width = frame.shape[:2]
    roi_vertices = np.array([[(100, height), (width//2, height//2), (width-100, height)]])
    cropped = region_of_interest(edges, roi_vertices)

    lines = cv2.HoughLinesP(cropped, 2, np.pi/180, 50, minLineLength=100, maxLineGap=50)
    result = draw_lines(frame, lines)
    return result
