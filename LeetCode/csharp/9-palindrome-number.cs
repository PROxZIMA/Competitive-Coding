using System.Collections;

namespace SDE_Sheet;

public class P9
{
    private static bool IsPalindrome(int x)
    {
        if (x < 0) return false;

        var original = x;
        var palindrome = 0;
        while (x > 0)
        {
            palindrome = (palindrome * 10) + (x % 10);
            x /= 10;
        }
        return palindrome == original;
    }

    private static bool IsPalindromeN(int x)
    {
        if (x < 0) return false;
        var nums = new List<int>();
        while (true)
        {
            if (x == 0) break;
            var r = x % 10;
            nums.Add(r);
            x /= 10;
        }

        (var i, var j) = (0, nums.Count - 1);
        while (i <= j)
        {
            if (nums[i] != nums[j]) return false;
            i++;
            j--;
        }

        return true;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            5,
            true
            };

            yield return new object[]
            {
            0,
            true
            };

            yield return new object[]
            {
            121,
            true
            };

            yield return new object[]
            {
            -121,
            false
            };

            yield return new object[]
            {
            10,
            false
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int nums, bool expected)
    {
        Assert.Equal(expected, IsPalindrome(nums));
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test2(int nums, bool expected)
    {
        Assert.Equal(expected, IsPalindromeN(nums));
    }
}