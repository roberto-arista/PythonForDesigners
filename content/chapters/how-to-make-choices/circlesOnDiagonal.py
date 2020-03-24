newPage(200, 200)

firstLightThenDark = True
circles = 4
radius = 32

stroke(0)
strokeWidth(4)

if firstLightThenDark is True:
    factorStep = 1 / (circles+1) 
    factor = factorStep
else:
    factorStep = -(1 / (circles+1))
    factor = 1 + factorStep

fill(1 - factor)
oval(width()*factor-radius, height()*factor-radius, radius*2, radius*2)
# factor = factor + factorStep
factor += factorStep

fill(1 - factor)
oval(width()*factor-radius, height()*factor-radius, radius*2, radius*2)
factor += factorStep

fill(1 - factor)
oval(width()*factor-radius, height()*factor-radius, radius*2, radius*2)
factor += factorStep

fill(1 - factor)
oval(width()*factor-radius, height()*factor-radius, radius*2, radius*2)
