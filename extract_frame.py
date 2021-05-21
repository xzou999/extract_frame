import cv2
import os
import sys
import getopt


def doExtract(argv):
    input_file = '';
    output_dir = '';
    fps = 1;

    try:
        opts, args = getopt.getopt(argv, "hi:o:f:", ["ifile=", "odir=", "fps="])
    except getopt.GetoptError:
        print("python extract_frame.py -i <inputfile> -o <outputdir> -f <fps>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('python extract_frame.py -i <inputfile> -o <outputdir> -f <fps>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--odir"):
            output_dir = arg
        elif opt in ("-f", "--fps"):
            fps = arg

    print("input file: {}".format(input_file))
    print("output_dir: {}".format(output_dir))

    #sourceFileName='05_simple_18'
    #video_path = os.path.join("", "", sourceFileName+'.mp4')
    video_path = input_file

    times=0
    sequential_num = 0

    print("video_path:{}".format(video_path))

    frameFrequency = int(fps)

    outPutDirName = output_dir + '/'

    if not os.path.exists(outPutDirName):
        os.makedirs(outPutDirName)
    camera = cv2.VideoCapture(video_path)
    while True:
        times+=1
        res, image = camera.read()
        if not res:
            print('not res , not image')
            break
        if times%frameFrequency==0:
            sequential_num += 1
            cv2.imwrite(outPutDirName + str(sequential_num)+'.jpg', image)
            print(outPutDirName + str(sequential_num)+'.jpg')

    print('done')
    camera.release()


if __name__ == "__main__":
    print(sys.argv)
    if (len(sys.argv) <= 1):
        print("python extract_frame.py -i <inputfile> -o <outputdir> -f <fps>")
        sys.exit(1)
    doExtract(sys.argv[1:])
