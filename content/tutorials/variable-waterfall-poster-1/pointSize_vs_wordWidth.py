#!/usr/bin/env python3

import drawBot as dB

testWord = 'hello world!'

dB.font('Skia', 1)
pointOneWdt, _ = dB.textSize(testWord)

dB.font('Skia', 1000)
pointOneThousandWdt, _ = dB.textSize(testWord)

assert pointOneWdt * 1000 == pointOneThousandWdt
# no error! 🎉
