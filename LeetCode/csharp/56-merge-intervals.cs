using System.Collections;

namespace SDE_Sheet;

public class P56
{
    private static void Solution(int[] nums)
    {
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 2,3,1,3,3 },
            new int[] { 2,3,1,3,3 }
            };

            yield return new object[]
            {
            new int[] { 1,1 },
            new int[] { 1,1 }
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, int[] expected)
    {
        Solution(nums);
        Assert.Equal(expected, nums);
    }
}