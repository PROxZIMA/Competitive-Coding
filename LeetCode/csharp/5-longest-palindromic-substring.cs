using System.Collections;

namespace SDE_Sheet;

public class P5
{
    private static string Solution(string s)
    {
        /*
        babad
          0 1 2 3 4
        0 T F T F F
        1   T F T F
        2     T F F
        3       T F
        4         T
        */
        (var resultIndex, var resultRange) = (0, 0);
        var dp = new bool[s.Length, s.Length];
        for (int i = 0; i < s.Length; i++)
        {
            for (int j = 0; j <= i; j++)
            {
                dp[j, i] = IsPalindrome(j, i);
                if (dp[j, i] && i - j > resultRange)
                {
                    resultIndex = j;
                    resultRange = i - j;
                }
            }
        }

        return s[resultIndex..(resultIndex + resultRange + 1)];

        bool IsPalindrome(int start, int end)
        {
            if (start == end) return true;
            if (Math.Abs(end - start) == 1) return s[start] == s[end];
            return s[start] == s[end] && dp[start + 1, end - 1];
        }
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            "abcdcbabc",
            "abcdcba"
            };

            yield return new object[]
            {
            "babad",
            "bab"
            };

            yield return new object[]
            {
            "a",
            "a"
            };

            yield return new object[]
            {
            "aa",
            "aa"
            };

            yield return new object[]
            {
            "ac",
            "a"
            };

            yield return new object[]
            {
            "cbbd",
            "bb"
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(string nums, string expected)
    {
        Assert.Equal(expected, Solution(nums));
    }
}