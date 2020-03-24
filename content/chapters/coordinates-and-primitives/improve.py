start = 10
end = 90

newPage(100, 100)
stroke(0)
strokeWidth(2)
# three parallel horizontal lines
# their points share the x values
line((start, 20), (end, 20))
line((start, 50), (end, 50))
line((start, 80), (end, 80))