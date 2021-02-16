from cover import assembleImages

if __name__ == '__main__':
    assembleImages(horElems=1,
                   verElems=1,
                   scalingFactor=.75,
                   inputPath='backCover.pdf',
                   outputPath='instagram_1.png',
                   margin=80,
                   _format=(1080, 1080))

    assembleImages(horElems=3,
                   verElems=2,
                   scalingFactor=.3,
                   inputPath='backCover.pdf',
                   outputPath='instagram_2.png',
                   margin=80,
                   _format=(1080, 1080))

    assembleImages(horElems=6,
                   verElems=4,
                   scalingFactor=.15,
                   inputPath='backCover.pdf',
                   outputPath='instagram_3.png',
                   margin=80,
                   _format=(1080, 1080))

    assembleImages(horElems=2,
                   verElems=3,
                   scalingFactor=.24,
                   inputPath='backCover.pdf',
                   outputPath='instagram_story_1.png',
                   margin=75,
                   _format=(1080, 1920))

    assembleImages(horElems=3,
                   verElems=4,
                   scalingFactor=.24,
                   inputPath='backCover.pdf',
                   outputPath='instagram_story_2.png',
                   margin=75,
                   _format=(1080, 1920))

    assembleImages(horElems=4,
                   verElems=5,
                   scalingFactor=.24,
                   inputPath='backCover.pdf',
                   outputPath='instagram_story_3.png',
                   margin=75,
                   _format=(1080, 1920))
