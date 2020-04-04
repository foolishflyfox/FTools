#!env python
import cv2, argparse, os, sys

if __name__ == "__main__":
    desc = 'Convert colorful image to gray image and save it in current folder.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('src_img', help='Source image path')
    # parser.add_argument('output', nargs='?', help='Output folder or path',
                            # default=None)
    args = parser.parse_args()
    img_path = args.src_img
    if not os.path.isfile(img_path):
        print("ERROR: {} isn't a file".format(img_path), file=sys.stderr)
        exit(1)
    src_suffix = os.path.splitext(img_path)[-1][1:]
    supported_format = ['png','jpg','jpeg','bmp', 'tif']
    if src_suffix.lower() not in supported_format:
        print('ERROR: Only support {}'.format('/'.join(supported_format)), 
                file=sys.stderr)
        exit(1)
    # get filename without suffix
    src_filename = os.path.splitext(os.path.split(img_path)[1])[0]
    try:
        img = cv2.imread(img_path)
        # width,height = img.shape[:2][::-1]
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('{}-gray.{}'.format(src_filename, src_suffix), img_gray)
    except cv2.error:
        print('ERROR: Fail to convert image {}'.format(img_path),
                file=sys.stderr)
        exit(-1)
    print('Convert successfully')
    