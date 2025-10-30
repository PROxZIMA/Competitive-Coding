using System.Collections;

namespace SDE_Sheet;

public class P3
{
    private static int Solution(string s)
    {
        var start = 0;
        var max = int.MinValue;
        var hashmap = new Dictionary<int, int>();

        for (int i = 0; i < s.Length; i++)
        {
            var key = (int)s[i];

            if (hashmap.TryGetValue(key, out var index))
            {
                max = Math.Max(max, i - start);
                for (int j = start; j <= index; j++)
                {
                    hashmap.Remove(s[j]);
                }
                start = index + 1;
            }
            hashmap[key] = i;
        }

        max = Math.Max(max, s.Length - start);
        return max;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            "abcabcbb",
            3
            };

            yield return new object[]
            {
            "bbbbb",
            1
            };

            yield return new object[]
            {
            "pwwkew",
            3
            };

            yield return new object[]
            {
            "",
            0
            };

            yield return new object[]
            {
            "abc",
            3
            };

            yield return new object[]
            {
            "aab",
            2
            };

            yield return new object[]
            {
            "abba",
            2
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(string s, int expected)
    {
        Assert.Equal(expected, Solution(s));
    }
}