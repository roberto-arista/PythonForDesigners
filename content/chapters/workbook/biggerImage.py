fileName = 'protractor.pdf'
scalingFactor = 4

wdt, hgt = imageSize(fileName)
newPage(wdt*scalingFactor, hgt*scalingFactor)
scale(scalingFactor)
image(fileName, (0, 0))
saveImage('protractor.png')