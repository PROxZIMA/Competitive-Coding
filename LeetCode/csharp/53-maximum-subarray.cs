using System.Collections;

namespace SDE_Sheet;

public class P53
{
    public int MaxSubArray(int[] nums)
    {
        var n = nums.Length;
        if (n == 1) return nums[0];

        var max = int.MinValue;
        var currentTotal = 0;
        foreach (var num in nums)
        {
            currentTotal = Math.Max(num, currentTotal + num);
            max = Math.Max(max, currentTotal);
        }
        return max;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { -2,1,-3,4,-1,2,1,-5,4 },
            6
            };

            yield return new object[]
            {
            new int[] { 1 },
            1
            };

            yield return new object[]
            {
            new int[] { -1, -2 },
            -1
            };

            yield return new object[]
            {
            new int[] { 1, 2 },
            3
            };

            yield return new object[]
            {
            new int[] { 5,4,-1,7,8 },
            23
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, int expected)
    {
        Assert.Equal(expected, MaxSubArray(nums));
    }
}