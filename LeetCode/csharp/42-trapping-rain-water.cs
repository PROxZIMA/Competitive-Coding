using System.Collections;

namespace SDE_Sheet;

public class P42
{
    private static int Trap(int[] height)
    {
        (var maxHeightIndex, var maxHeight) = (0, int.MinValue);
        for (int i = 0; i < height.Length; i++)
        {
            if (height[i] > maxHeight)
            {
                maxHeight = height[i];
                maxHeightIndex = i;
            }
        }

        // from ith index to jth index where nums[j] >= nums[i]
        // result += total area ((j-i)*nums[i]) - filled block sum(nums[i]...nums[j])
        var result = 0;
        var blockStart = 0;
        var blockedArea = height[blockStart];

        for (int j = 1; j <= maxHeightIndex; j++)
        {
            blockedArea += Math.Min(height[blockStart], height[j]);
            if (height[j] >= height[blockStart])
            {
                result += (j - blockStart + 1) * height[blockStart] - blockedArea;
                blockedArea = height[j];
                blockStart = j;
            }
        }
        blockStart = height.Length - 1;
        blockedArea = height[blockStart];
        for (int j = height.Length - 2; j >= maxHeightIndex; j--)
        {
            blockedArea += Math.Min(height[blockStart], height[j]);
            if (height[j] >= height[blockStart])
            {
                result += (blockStart - j + 1) * height[blockStart] - blockedArea;
                blockedArea = height[j];
                blockStart = j;
            }
        }
        return result;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 0 },
            0
            };

            yield return new object[]
            {
            new int[] { 6,1 },
            0
            };

            yield return new object[]
            {
            new int[] { 1,6 },
            0
            };

            yield return new object[]
            {
            new int[] { 5 },
            0
            };

            yield return new object[]
            {
            new int[] { 0,1,0,2,1,0,1,3,2,1,2,1 },
            6
            };

            yield return new object[]
            {
            new int[] { 4,2,0,3,2,5 },
            9
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, int expected)
    {
        Assert.Equal(expected, Trap(nums));
    }
}