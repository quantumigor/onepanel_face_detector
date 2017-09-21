import dlib
from skimage import io


def apply(input_data):
    detector = dlib.get_frontal_face_detector()
    faces_bb = {}

    try:
        img = io.imread(input_data["image"]["url"])
    except:
        faces_bb[str(0)] = "Error, while trying to read file"
        return faces_bb
    dets = detector(img, 1)

    if len(dets) > 0:
        for i, d in enumerate(dets):
            faces_bb[str(i)] = {"left": d.left(), "top": d.top(), "right": d.right(), "bottom": d.bottom()}
    else:
        faces_bb[str(0)] = "No faces detected"
    return faces_bb


test_dict = {"image": {"url": "http://whatis.techtarget.com/fileformat/TXT-ASCII-text-formatted-data"}}
print(apply(test_dict))
