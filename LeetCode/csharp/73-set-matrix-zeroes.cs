using System.Collections;

namespace SDE_Sheet;

public class P73
{
    private static void SetZeroes(int[][] matrix)
    {
        var m = matrix.Length;
        var n = matrix[0].Length;

        var firstRowHasZero = false;
        var firstColHasZero = false;

        for (var i = 0; i < m; i++)
        {
            for (var j = 0; j < n; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;

                    if (i == 0 && !firstRowHasZero) firstRowHasZero = true;
                    if (j == 0 && !firstColHasZero) firstColHasZero = true;
                }

            }
        }

        for (var i = 1; i < m; i++)
        {
            for (var j = 1; j < n; j++)
            {
                if (matrix[0][j] == 0 ||
                    matrix[i][0] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
        }

        if (matrix[0][0] == 0)
        {
            if (firstRowHasZero)
                for (var j = 1; j < n; j++)
                {
                    matrix[0][j] = 0;
                }

            if (firstColHasZero)
                for (var i = 1; i < m; i++)
                {
                    matrix[i][0] = 0;
                }
        }
    }

    private static void SetZeroesMpN(int[][] matrix)
    {
        var m = matrix.Length;
        var n = matrix[0].Length;

        HashSet<int> rowIds = [];
        HashSet<int> colIds = [];

        for (var i = 0; i < m; i++)
        {
            for (var j = 0; j < n; j++)
            {
                if (matrix[i][j] == 0)
                {
                    rowIds.Add(i);
                    colIds.Add(j);
                }
            }
        }

        for (var i = 0; i < m; i++)
        {
            for (var j = 0; j < n; j++)
            {
                if (rowIds.Contains(i) ||
                    colIds.Contains(j))
                {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    private class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[][] { [1,1,1],[1,0,1],[1,1,1] },
            new int[][] { [1,0,1],[0,0,0],[1,0,1] }
            };

            yield return new object[]
            {
            new int[][] { [0,1,2,0],[3,4,5,2],[1,3,1,5] },
            new int[][] { [0,0,0,0],[0,4,5,0],[0,3,1,0] },
            };

            yield return new object[]
            {
            new int[][] { [1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0] },
            new int[][] { [0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0] },
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[][] nums, int[][] expected)
    {
        SetZeroes(nums);
        Assert.Equal(expected, nums);
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test2(int[][] nums, int[][] expected)
    {
        SetZeroesMpN(nums);
        Assert.Equal(expected, nums);
    }
}