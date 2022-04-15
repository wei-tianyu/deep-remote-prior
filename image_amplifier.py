import cv2
import numpy as np

#pt1: upper-left point of region to amplify
#pt2: lower-right
#ratio: how large to amplify
#pos = 'LR', 'LL', 'UR', 'UL' where to put the amplified image
#Usage: amplify_rec('data/denoising/image_Lena512rgb.png', (150, 70), (250, 130), 'LR')
def amplify_rec(filepath, destpath, pt1, pt2,  height, width = 143, ratio = 2,  pos = 'LR'):
    image = cv2.imread(filepath)
    print(type(image))
    print(image.shape)
    patch1 = image[pt1[1]:pt1[1] + height,  pt1[0]:pt1[0] + width :]
    patch2 = image[pt2[1]:pt2[1] + height, pt2[0]:pt2[0] + width, :]
    cv2.rectangle(image, pt1, (pt1[0] + width, pt1[1] + height), (0, 0, 255), 2)
    cv2.rectangle(image, pt2, (pt2[0] + width, pt2[1] + height), (255, 0, 0), 2)
    patch1 = cv2.resize(patch1, (ratio*width, ratio*height))
    patch2 = cv2.resize(patch2, (ratio*width, ratio*height))
    result_width = image.shape[1]
    result_height = ratio*height + 2 + image.shape[0]
    result = np.ones((result_height, result_width, 3)) * 255
    result[0 : image.shape[0], :] = image
    result[result_height-ratio*height:result_height, 0:ratio*width] = patch1
    result[result_height-ratio*height:result_height, result_width-ratio*width:result_width] = patch2
    cv2.imwrite(destpath, result)

# amplify_rec('optimal for lena/optimal_gt_sm_pgd_ad.png', 'amp_lena/optimal_gt_sm_pgd_ad.png', (180, 160), (310, 270))
# amplify_rec('optimal for lena/optimal_gt_sm_dip.png', 'amp_lena/optimal_gt_sm_dip.png', (180, 160), (310, 270))
# amplify_rec('optimal for lena/optimal_gt_dip.png', 'amp_lena/optimal_gt_dip.png', (180, 160), (310, 270))
# amplify_rec('optimal for lena/optimal_gt_pgd_ad.png', 'amp_lena/optimal_gt_pgd_ad.png', (180, 160), (310, 270))
# amplify_rec('optimal for lena/noisy_lena.png', 'amp_lena/noisy_lena.png', (180, 160), (310, 270))
amplify_rec('zebra_dip_optimal.png', 'zebra_ampli_dip.png', (80, 120), (400, 120), 50)
amplify_rec('zebra_pdp_optimal.png', 'zebra_ampli_pdp.png', (80, 120), (400, 120), 50)
amplify_rec('original.png', 'zebra_original.png', (80, 120), (400, 120), 50)