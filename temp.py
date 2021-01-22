from trdg.generators import GeneratorFromWikipedia, GeneratorFromTextFile
import numpy as np

if __name__ == '__main__':
    import cv2
    generator = GeneratorFromTextFile(folder='./trdg/dicts/', count=-1, size=(30, 70), language='en',
                                      minimum_length=1, maximum_length=10,
                                      skewing_angle=2, random_skew=True, blur=1, random_blur=True,
                                      background_type=3, distorsion_type=-1, margins=(2, 2, 2, 2))

    print('Start generating ...')
    for i, (img, lbl) in enumerate(generator):
        img_path = './data/generated/' + str(i) + '.png'
        # cv2.imwrite(img_path, np.array(img))
        print(img_path, lbl)