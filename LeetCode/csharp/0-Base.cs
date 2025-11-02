using System.Collections;

namespace SDE_Sheet;

public class P0
{
    private static int Solution(int[] nums)
    {
        return 1;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 2,3,1,3,3 },
            1
            };

            yield return new object[]
            {
            new int[] { 1,1 },
            1
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, int expected)
    {
        Assert.Equal(expected, Solution(nums));
    }
}