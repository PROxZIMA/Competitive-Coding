using System.Collections;

namespace SDE_Sheet;

public class P4
{
    private static double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        (var l1, var l2) = (nums1.Length, nums2.Length);
        // Search in shorter array first to prevent out of index
        if (l1 > l2) return FindMedianSortedArrays(nums2, nums1);

        var isOdd = (l1 + l2) % 2 == 1;
        (var low, var high) = (0, l1);
        int medianIndex = (l1 + l2 + 1) / 2;
        
        while (low <= high)
        {
            int partitian1 = (low + high) / 2;
            int partitian2 = medianIndex - partitian1;

            var maxLeft1 = partitian1 <= 0
                            ? int.MinValue
                            : nums1[partitian1 - 1];
            var minRight1 = partitian1 >= l1
                            ? int.MaxValue
                            : nums1[partitian1];
            var maxLeft2 = partitian2 <= 0
                            ? int.MinValue
                            : nums2[partitian2 - 1];
            var minRight2 = partitian2 >= l2
                            ? int.MaxValue
                            : nums2[partitian2];

            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1)
            {
                return isOdd
                    ? Math.Max(maxLeft1, maxLeft2)
                    : (double)(Math.Max(maxLeft1, maxLeft2) + Math.Min(minRight1, minRight2)) / 2;
            }

            if (maxLeft1 > minRight2)
            {
                high = partitian1 - 1;
            }

            if (maxLeft2 > minRight1)
            {
                low = partitian1 + 1;
            }
        }
        return 0;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 1,3,8 },
            new int[] { 7,9,10,11 },
            8.0
            };

            yield return new object[]
            {
            new int[] { 1,3 },
            new int[] { 2 },
            2.0
            };

            yield return new object[]
            {
            new int[] { 1,2 },
            new int[] { 3,4 },
            2.5
            };

            yield return new object[]
            {
            new int[] { },
            new int[] { 2 },
            2
            };

            yield return new object[]
            {
            new int[] { 2 },
            new int[] { },
            2
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums1, int[] nums2, double expected)
    {
        Assert.Equal(expected, FindMedianSortedArrays(nums1, nums2));
    }
}