import os
import sys

def countMax(upRight):
    def countMax(upRight):
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input())

        steps = []

        for _ in range(n):
            steps.append(list(map(int, input().rstrip().split())))

        result = solve(steps)

        fptr.write(str(result) + '\n')

        fptr.close()