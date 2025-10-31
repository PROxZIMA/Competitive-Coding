using System.Collections;

namespace SDE_Sheet;

public class P14
{
    private static string LongestCommonPrefix(string[] strs)
    {
        var longestPrefix = strs[0];
        foreach(var str in strs)
        {
            var searchIndex = Math.Min(longestPrefix.Length, str.Length);
            var index = 0;
            while (index < searchIndex)
            {
                if (longestPrefix[index] != str[index]) break;
                index++;
            }
            longestPrefix = longestPrefix[0..index];
            if (index == 0) break;
        }
        return longestPrefix;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new string[] { "flower","flow","flight" },
            "fl"
            };

            yield return new object[]
            {
            new string[] { "dog","racecar","car" },
            ""
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(string[] nums, string expected)
    {
        Assert.Equal(expected, LongestCommonPrefix(nums));
    }
}