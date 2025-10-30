using System.Collections;

namespace SDE_Sheet;

public class P1
{
    private static int[] Solution(int[] nums, int target)
    {
        Assert.InRange(nums.Length, 2, int.MaxValue);

        var hash = new Dictionary<int, int>();
        for (var i = 0; i < nums.Length; i++)
        {
            hash[nums[i]] = i;
        }

        for (var i = 0; i < nums.Length; i++)
        {
            if (hash.TryGetValue(target - nums[i], out var index) && i != index)
            {
                return [i, index];
            }
        }
        throw new Exception("Solution not found");
    }

    private static int[] SolutionN2(int[] nums, int target)
    {
        Assert.InRange(nums.Length, 2, int.MaxValue);

        for (var i = 0; i < nums.Length; i++)
        {
            for (var j = i + 1; j < nums.Length; j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    return [i, j];
                }
            }
        }
        throw new Exception("Solution not found");
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 2,7,11,15 },
            9,
            new int[] { 0,1 }
            };

            yield return new object[]
            {
            new int[] { 3,2,4 },
            6,
            new int[] { 1,2 }
            };

            yield return new object[]
            {
            new int[] { 3,3 },
            6,
            new int[] { 0,1 }
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, int target, int[] expected)
    {
        Assert.Equal(expected, Solution(nums, target));
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test2(int[] nums, int target, int[] expected)
    {
        Assert.Equal(expected, SolutionN2(nums, target));
    }
}