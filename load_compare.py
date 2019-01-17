import cv2
import numpy as np


def load(fname):
    img = cv2.imread(fname)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def save_color(fname, img):
    cv2.imwrite(fname, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))


def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def rescale(img):
    return cv2.resize(img, (84, 84), interpolation=cv2.INTER_AREA)


def list_colors_in_frame(img):
    colors = set()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j].shape:
                colors.add(tuple(img[i, j]))
            else:
                colors.add(img[i, j])

    return sorted(colors)


def typical_preprocessing(img):
    return rescale(to_gray(img))


def collage(img_one, img_two):
    return np.hstack([img_one, img_two])


if __name__ == '__main__':
    img_fname_agc = 'data/agc_1.png'
    img_fname_gym = 'data/gym_1.png'

    # get color list
    print("colors in agc        = {}".format(list_colors_in_frame(load(img_fname_agc))))
    print("colors in openai gym = {}".format(list_colors_in_frame(load(img_fname_gym))))

    save_color('color_comparison.png', collage(load(img_fname_agc), load(img_fname_gym)))

    cv2.imwrite(
        'processed_comparison.png',
        collage(
            typical_preprocessing(load(img_fname_agc)),
            typical_preprocessing(load(img_fname_gym))
        )
    )


