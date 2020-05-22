import os

import cv2

from music_detection.StaffRemover import staffDetection


def test_count_staves_successfully():
    path = os.path.dirname(os.path.abspath(__file__))
    image = cv2.imread(os.path.join(path, "../resources/test_images/twinkle.jpg"))
    staves, _ = staffDetection(image)
    assert len(staves) == 3