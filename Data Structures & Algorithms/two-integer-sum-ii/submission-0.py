class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        front = 0
        back = n
        while front != back:
            if numbers[front] + numbers[back] > target:
                back -= 1
            elif numbers[front] + numbers[back] < target:
                front += 1
            else:
                return [front + 1, back + 1]
        