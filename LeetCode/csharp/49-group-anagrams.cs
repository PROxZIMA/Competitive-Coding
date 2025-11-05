using System.Collections;

namespace SDE_Sheet;

public class P49
{
    private static IList<IList<string>> GroupAnagrams(string[] strs)
    {
        var sortedStrs = new string[strs.Length];

        for (int i = 0; i < strs.Length; i++)
        {
            var arr = strs[i].ToCharArray();
            Array.Sort(arr);
            sortedStrs[i] = new string(arr);
        }

        var counterMap = new Dictionary<string, List<string>>();
        for (int i = 0; i < strs.Length; i++)
        {
            var sortedStr = sortedStrs[i];
            if (counterMap.TryGetValue(sortedStr, out var occurences))
            {
                occurences.Add(strs[i]);
            }
            else
            {
                counterMap[sortedStr] = [strs[i]];
            }
        }

        return [..counterMap.Values.Select(v => v)];
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new string[] { "eat","tea","tan","ate","nat","bat" },
            new string[][] { ["eat", "tea", "ate"], ["tan", "nat"], ["bat"] }
            };

            yield return new object[]
            {
            new string[] { "a" },
            new string[][] { ["a"] }
            };

            yield return new object[]
            {
            new string[] { "" },
            new string[][] { [""] }
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(string[] nums, IList<IList<string>> expected)
    {
        Assert.Equal(expected, GroupAnagrams(nums));
    }
}