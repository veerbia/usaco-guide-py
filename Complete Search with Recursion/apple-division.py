# Apple Division

n = int(input())
weights = list(map(int, input().split()))

def solve(i, sum1, sum2):
	if i == n:
		return abs(sum2 - sum1)
	else:
		return min(solve(i+1, sum1 + weights[i], sum2), solve(i+1, sum1, sum2 + weights[i]))

print(solve(0,0,0))

# Time Complexity: O(2^n)
# Space Complexity: O(n)
