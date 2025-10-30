using System.Collections;

namespace SDE_Sheet;

public class P118
{
    private static IList<IList<int>> Generate(int numRows)
    {
        IList<IList<int>> result = [];

        for (var i = 0; i < numRows; i++)
        {
            if (i == 0)
            {
                result.Add([1]);
                continue;
            }

            IList<int> newArr = [1];
            for (var j = 0; j < i - 1; j++)
            {
                newArr.Add(result[i - 1][j] + result[i - 1][j + 1]);
            }
            newArr.Add(1);
            result.Add(newArr);
        }

        return result;
    }

    private class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            1,
            new int[][] { [1] }
            };

            yield return new object[]
            {
            5,
            new int[][] { [1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1] },
            };

            yield return new object[]
            {
            6,
            new int[][] { [1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1] },
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int numRows, IList<IList<int>> expected)
    {
        Assert.Equal(expected, Generate(numRows));
    }
}