using System.Collections;

namespace SDE_Sheet;

public class P15
{
    private static IList<IList<int>> ThreeSum(int[] nums)
    {
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { -1,0,1,2,-1,-4 },
            new int[][] { [-1,-1,2],[-1,0,1] }
            };

            yield return new object[]
            {
            new int[] { 0,1,1 },
            new int[][] { }
            };

            yield return new object[]
            {
            new int[] { 0,0,0 },
            new int[][] { [0,0,0] }
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, IList<IList<int>> expected)
    {
        Assert.Equivalent(expected, ThreeSum(nums));
    }
}