import sys
input = sys.stdin.readline

t = int(input())
# stars = [0]*t
# stars = [""]*t
stars = [" "]*t

for i in range(t):
  stars[i]="*"
  reversed_stars = reversed(stars)
  print(*reversed_stars,sep="")
