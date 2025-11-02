using System.Collections;
using System.Globalization;

namespace SDE_Sheet;

public class P162
{
    private static int FindPeakElement(int[] nums)
    {
        int FindLocalPeak(int start, int end)
        {
            if (start >= end) return end;
            int mid = start + (end - start) / 2;
            if (nums[mid] < nums[mid + 1])
            {
                return FindLocalPeak(mid + 1, end);
            }
            return FindLocalPeak(start, mid);
        }
        return FindLocalPeak(0, nums.Length - 1);
    }

    private static int FindPeakElementN(int[] nums)
    {
        if (nums.Length == 1) return 0;

        (var start, var end) = (1, nums.Length - 2);
        while (start <= end + 2)
        {
            if (nums[end] < nums[end + 1])
                return end + 1;
            if (nums[start] < nums[start - 1])
                return start - 1;
            start++;
            end--;
        }
        return -1;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 1 },
            0
            };

            yield return new object[]
            {
            new int[] { 2,1 },
            0
            };

            yield return new object[]
            {
            new int[] { 1,2,1 },
            1
            };

            yield return new object[]
            {
            new int[] { 1,2 },
            1
            };

            yield return new object[]
            {
            new int[] { 1,2,3,1 },
            2
            };

            yield return new object[]
            {
            new int[] { 1,2,1,3,5,6,4 },
            5
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, int expected)
    {
        Assert.Equal(expected, FindPeakElement(nums));
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test2(int[] nums, int expected)
    {
        Assert.Equal(expected, FindPeakElementN(nums));
    }
}