using System.Collections;
using Newtonsoft.Json;

namespace SDE_Sheet;

public class P169
{
    private static int MajorityElement(int[] nums)
    {
        (int frequency, int majorityElement) = (0, 0);
        foreach (int num in nums)
        {
            if (frequency == 0)
            {
                majorityElement = num;
            }
            if (num == majorityElement)
            {
                frequency++;
            }
            else
            {
                frequency--;
            }
        }

        return majorityElement;
    }

    private static int SolutionNlogN(int[] nums)
    {
        Array.Sort(nums);
        return nums[nums.Length / 2];
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 6,6,6,7,7 },
            6
            };

            yield return new object[]
            {
            new int[] { 2,2,1,3,1,1,4,1,1,5,1,1,6 },
            1
            };

            yield return new object[]
            {
            new int[] { 2,2,1 },
            2
            };

            yield return new object[]
            {
            new int[] { 1,2,2 },
            2
            };

            yield return new object[]
            {
            new int[] { 1,2,3,4,4,4,4 },
            4
            };

            yield return new object[]
            {
            new int[] { 4,1,4,2,3,4,4 },
            4
            };

            yield return new object[]
            {
            new int[] { 3,2,3 },
            3
            };

            yield return new object[]
            {
            new int[] { 2,2,1,1,1,2,2 },
            2
            };

            yield return new object[]
            {
            new int[] { 1,2,1,1,1,2,2 },
            1
            };

            yield return new object[]
            {
            new int[] { 1,2,1,1,1,2 },
            1
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, int expected)
    {
        Assert.Equal(expected, MajorityElement(nums));
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test2(int[] nums, int expected)
    {
        Assert.Equal(expected, SolutionNlogN(nums));
    }
}