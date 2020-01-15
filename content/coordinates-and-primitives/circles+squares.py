newPage(100, 100)

radius = 20

fill(.2)
rect(0, 0, radius, radius)
rect(width()-radius, 0, radius, radius)
rect(width()-radius, height()-radius, radius, radius)
rect(0, height()-radius, radius, radius)

fill(.6)
oval(-radius, -radius, radius*2, radius*2)
oval(width()-radius, -radius, radius*2, radius*2)
oval(width()-radius, height()-radius, radius*2, radius*2)
oval(-radius, height()-radius, radius*2, radius*2)