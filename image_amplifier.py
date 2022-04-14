import cv2
import numpy as np

#pt1: upper-left point of region to amplify
#pt2: lower-right
#ratio: how large to amplify
#pos = 'LR', 'LL', 'UR', 'UL' where to put the amplified image
#Usage: amplify_rec('data/denoising/image_Lena512rgb.png', (150, 70), (250, 130), 'LR')
def amplify_rec(filepath, destpath, pt1, pt2, ratio = 2,  pos = 'LR'):
    image = cv2.imread(filepath)
    cv2.rectangle(image, pt1, pt2, (0, 0, 255), 2)
    patch1 = image[pt1[1]:pt2[1], pt1[0]:pt2[0], :]
    patch1 = cv2.resize(patch1, (ratio*patch1.shape[1], 2*patch1.shape[0]))
    width = patch1.shape[1]
    height = patch1.shape[0]
    if pos == 'UL':  #UPPER LEFT
        image[0:height, 0:width] = patch1
    elif pos == 'LL': #LOWER LEFT
        image[image.shape[0]-height:image.shape[0], 0:width] = patch1
    elif pos == 'UR': #UPPER RIGHT
        image[0:height, image.shape[1]-width:image.shape[1]] = patch1
    else:
        image[image.shape[0]-height:image.shape[0], image.shape[1]-width:image.shape[1]] = patch1
    cv2.imshow('demo', image)
    cv2.imwrite(destpath, image)

amplify_rec('optimal for lena/optimal_gt_sm_pgd_ad.png', 'amp_lena/optimal_gt_sm_pgd_ad.png', (180, 160), (310, 270))
amplify_rec('optimal for lena/optimal_gt_sm_dip.png', 'amp_lena/optimal_gt_sm_dip.png', (180, 160), (310, 270))
amplify_rec('optimal for lena/optimal_gt_dip.png', 'amp_lena/optimal_gt_dip.png', (180, 160), (310, 270))
amplify_rec('optimal for lena/optimal_gt_pgd_ad.png', 'amp_lena/optimal_gt_pgd_ad.png', (180, 160), (310, 270))
amplify_rec('optimal for lena/noisy_lena.png', 'amp_lena/noisy_lena.png', (180, 160), (310, 270))