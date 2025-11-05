using System.Collections;

namespace SDE_Sheet;

public class P53
{
    public int MaxSubArray(int[] nums)
    {
        var result = nums[0];
        var currMaximum = nums[0];

        for (int i = 1; i < nums.Length; i++)
        {
            currMaximum = Math.Max(nums[i], currMaximum + nums[i]);
            result = Math.Max(result, currMaximum);
        }

        return result;
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