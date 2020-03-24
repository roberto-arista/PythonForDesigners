newPage(400, 400)

quota = height()/2
radius = 20
module = width()/5
grayModule = 1/5

# 1
fill(grayModule*1)
xx = module*1
oval(xx-radius, quota-radius, radius*2, radius*2)

# 2
fill(grayModule*2)
xx = module*2
oval(xx-radius, quota-radius, radius*2, radius*2)

# 3
fill(grayModule*3)
xx = module*3
oval(xx-radius, quota-radius, radius*2, radius*2)

# 4
fill(grayModule*4)
xx = module*4
oval(xx-radius, quota-radius, radius*2, radius*2)