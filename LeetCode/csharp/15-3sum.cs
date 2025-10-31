using System.Collections;

namespace SDE_Sheet;

public class P15
{
    private static IList<IList<int>> ThreeSum(int[] nums)
    {
        var result = new HashSet<(int i, int j, int k)>();
        Array.Sort(nums);
        for (int i = 0; i < nums.Length - 2; i++)
        {
            (var j, var k) = (i + 1, nums.Length - 1);

            while (j < k)
            {
                var total = nums[i] + nums[j] + nums[k];
                if (total == 0)
                {
                    var key = new int[] { nums[i], nums[j], nums[k] };
                    Array.Sort(key);
                    result.Add((key[0], key[1], key[2]));
                    j++;
                    k--;
                }
                else if (total < 0)
                {
                    j++;
                }
                else
                {
                    k--;
                }
            }
        }
        return [.. result.Select<(int i, int j, int k), IList<int>>(r => new List<int>([r.i, r.j, r.k]))];
    }

    private static IList<IList<int>> ThreeSumN2(int[] nums)
    {
        var result = new HashSet<(int i, int j, int k)>();
        var lookup = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            lookup[nums[i]] = i;
        }
        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = i + 1; j < nums.Length; j++)
            {
                var toLookup = -(nums[i] + nums[j]);
                if (lookup.TryGetValue(toLookup, out var k) && k > j)
                {
                    var key = new List<int>([nums[i], nums[j], nums[k]]);
                    key.Sort();
                    result.Add((key[0], key[1], key[2]));
                }
            }
        }
        return [.. result.Select<(int i, int j, int k), IList<int>>(r => new List<int>([r.i, r.j, r.k]))];
    }

    private static IList<IList<int>> ThreeSumN3(int[] nums)
    {
        var result = new HashSet<(int i, int j, int k)>();
        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = i + 1; j < nums.Length; j++)
            {
                for (int k = j + 1; k < nums.Length; k++)
                {
                    if (nums[i] + nums[j] + nums[k] == 0)
                    {
                        var key = new List<int>([nums[i], nums[j], nums[k]]);
                        key.Sort();                        
                        result.Add((key[0], key[1], key[2]));
                    }
                }
            }
        }
        return [.. result.Select<(int i, int j, int k), IList<int>>(r => new List<int>([r.i, r.j, r.k]))];
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { -1,0,1,2,-1,-4 },
            new int[][] { [-1,-1,2],[-1,0,1] }
            };

            yield return new object[]
            {
            new int[] { 0,1,1 },
            new int[][] { }
            };

            yield return new object[]
            {
            new int[] { 0,0,0 },
            new int[][] { [0,0,0] }
            };

            yield return new object[]
            {
            new int[] { -1,0,1,2,-1,-4 },
            new int[][] { [-1,-1,2],[-1,0,1] }
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] nums, IList<IList<int>> expected)
    {
        Assert.Equivalent(expected, ThreeSum(nums), strict: true);
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test2(int[] nums, IList<IList<int>> expected)
    {
        Assert.Equivalent(expected, ThreeSumN2(nums), strict: true);
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test3(int[] nums, IList<IList<int>> expected)
    {
        Assert.Equivalent(expected, ThreeSumN3(nums), strict: true);
    }
}