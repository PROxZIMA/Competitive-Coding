using System.Collections;

namespace SDE_Sheet;

public class P88
{
    private static void Solution(int[] nums1, int m, int[] nums2, int n)
    {
        for (int _i = m - 1; _i >= 0; _i--)
        {
            nums1[n + _i] = nums1[_i];
        }
        (var i, var j) = (n, 0);
        var iter = 0;
        while (i < (m + n) && j < n)
        {
            if (nums1[i] <= nums2[j])
            {
                nums1[iter] = nums1[i];
                i++;
            }
            else
            {
                nums1[iter] = nums2[j];
                j++;
            }
            iter++;
        }
        while (i < (m + n))
        {
            nums1[iter] = nums1[i];
            iter++;
            i++;
        }
        while (j < n)
        {
            nums1[iter] = nums2[j];
            iter++;
            j++;
        }
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 1,2,3,4,0,0,0 },
            4,
            new int[] { 2,5,6 },
            3,
            new int[] { 1,2,2,3,4,5,6 }
            };

            yield return new object[]
            {
            new int[] { 1,2,3,0,0,0 },
            3,
            new int[] { 2,5,6 },
            3,
            new int[] { 1,2,2,3,5,6 }
            };

            yield return new object[]
            {
            new int[] { 1 },
            1,
            new int[] { },
            0,
            new int[] { 1 },
            };

            yield return new object[]
            {
            new int[] { 0 },
            0,
            new int[] { 1 },
            1,
            new int[] { 1 },
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums1, int m, int[] nums2, int n, int[] expected)
    {
        Solution(nums1, m, nums2, n);
        Assert.Equal(expected, nums1);
    }
}