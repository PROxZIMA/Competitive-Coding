using System.Collections;
using Newtonsoft.Json;

namespace SDE_Sheet;

public class P56
{
    public class Comparer : IComparer<int[]>
    {
        public int Compare(int[]? x, int[]? y)
        {
            if (x is null && y is null) return 0;
            if (x is null) return -1;
            if (y is null) return 1;
            if (x[0] > y[0]) return 1;
            if (x[0] < y[0]) return -1;
            if (x[1] > y[1]) return -1;
            if (x[1] < y[1]) return 1;
            return 0;
        }
    }
    private static int[][] Merge(int[][] intervals)
    {
        Array.Sort(intervals, new Comparer());
        var result = new List<List<int>>
        {
            ([intervals[0][0], intervals[0][1]])
        };

        for (int i = 1; i < intervals.Length; i++)
        {
            var interval = intervals[i];
            var lastInterval = result[^1];

            if (lastInterval[1] >= interval[1]) continue;
            if (lastInterval[1] >= interval[0])
            {
                result[^1] = [lastInterval[0], interval[1]];
                continue;
            }
            result.Add([interval[0], interval[1]]);
        }
        
        return [.. result.Select<List<int>, int[]>(i => [i[0], i[1]])];
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[][] { [2,5],[3,8],[1,3],[1,10] },
            new int[][] { [1,10] }
            };

            yield return new object[]
            {
            new int[][] { [8,10],[1,3],[2,6],[15,18] },
            new int[][] { [1,6],[8,10],[15,18] }
            };

            yield return new object[]
            {
            new int[][] { [1,4],[4,5] },
            new int[][] { [1,5] }
            };

            yield return new object[]
            {
            new int[][] { [4,7],[1,4] },
            new int[][] { [1,7] }
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[][] nums, int[][] expected)
    {
        Assert.Equal(expected, Merge(nums));
    }
}