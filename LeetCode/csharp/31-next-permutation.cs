using System.Collections;

namespace SDE_Sheet;

public class P31
{
    private static void NextPermutation(int[] nums)
    {
        var n = nums.Length;
        var i = n - 2;
        for (; i >= 0; i--)
        {
            var curr = nums[i];
            if (curr >= nums[i + 1]) continue;
 
            var currMax = int.MaxValue;
            var currMaxIdx = int.MaxValue;
            for (var j = i + 1; j < n; j++)
            {
                if (curr < nums[j] && nums[j] < currMax)
                {
                    currMax = nums[j];
                    currMaxIdx = j;
                }
            }

            (nums[i], nums[currMaxIdx]) = (nums[currMaxIdx], nums[i]);
            break;
        }

        Array.Sort(nums, i + 1, n - i - 1);
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 2,3,1,3,3 },
            new int[] { 2,3,3,1,3 }
            };

            yield return new object[]
            {
            new int[] { 1,1 },
            new int[] { 1,1 }
            };

            yield return new object[]
            {
            new int[] { 1,2,3 },
            new int[] { 1,3,2 }
            };

            yield return new object[]
            {
            new int[] { 1,3,2 },
            new int[] { 2,1,3 }
            };

            yield return new object[]
            {
            new int[] { 2,1,3 },
            new int[] { 2,3,1 }
            };

            yield return new object[]
            {
            new int[] { 2,3,1 },
            new int[] { 3,1,2 }
            };

            yield return new object[]
            {
            new int[] { 3,1,2 },
            new int[] { 3,2,1 }
            };

            yield return new object[]
            {
            new int[] { 3,2,1 },
            new int[] { 1,2,3 }
            };

            yield return new object[]
            {
            new int[] { 1,1,5 },
            new int[] { 1,5,1 }
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, int[] expected)
    {
        NextPermutation(nums);
        Assert.Equal(expected, nums);
    }
}