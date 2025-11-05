using System.Collections;

namespace SDE_Sheet;

public class P48
{
    private static void Rotate(int[][] matrix)
    {
        var n = matrix.Length;
        if (n == 1) return;

        int[][] locations =
        [
            [0,0],
            [0,n-1],
            [n-1,n-1],
            [n-1,0]
        ];

        for (var i = n; i > 1; i -= 2)
        {
            for (var j = 0; j < i - 1; j++)
            {
                int[][] newLocations =
                [
                    [locations[0][0], locations[0][1] + j],
                    [locations[1][0] + j, locations[1][1]],
                    [locations[2][0], locations[2][1] - j],
                    [locations[3][0] - j, locations[3][1]],
                ];

                (matrix[newLocations[0][0]][newLocations[0][1]],
                matrix[newLocations[3][0]][newLocations[3][1]],
                matrix[newLocations[2][0]][newLocations[2][1]],
                matrix[newLocations[1][0]][newLocations[1][1]]) =
                (matrix[newLocations[3][0]][newLocations[3][1]],
                 matrix[newLocations[2][0]][newLocations[2][1]],
                 matrix[newLocations[1][0]][newLocations[1][1]],
                 matrix[newLocations[0][0]][newLocations[0][1]]);
            }

            locations =
            [
                [locations[0][0] + 1, locations[0][1] + 1],
                [locations[1][0] + 1, locations[1][1] - 1],
                [locations[2][0] - 1, locations[2][1] - 1],
                [locations[3][0] - 1, locations[3][1] + 1],
            ];
        }
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[][] { [1] },
            new int[][] { [1] }
            };

            yield return new object[]
            {
            new int[][] { [1,2],[3,4] },
            new int[][] { [3,1],[4,2] }
            };

            yield return new object[]
            {
            new int[][] { [1,2,3],[4,5,6],[7,8,9] },
            new int[][] { [7,4,1],[8,5,2],[9,6,3] }
            };

            yield return new object[]
            {
            new int[][] { [5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16] },
            new int[][] { [15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11] }
            };

            yield return new object[]
            {
            new int[][] { [43,39,3,33,37,20,14],[9,18,9,-1,40,22,38],[14,42,3,23,12,14,32],[18,31,45,11,8,-1,31],[28,44,14,23,40,24,13],[29,45,33,45,20,0,45],[12,23,35,32,22,39,8] },
            new int[][] { [12,29,28,18,14,9,43],[23,45,44,31,42,18,39],[35,33,14,45,3,9,3],[32,45,23,11,23,-1,33],[22,20,40,8,12,40,37],[39,0,24,-1,14,22,20],[8,45,13,31,32,38,14] }
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[][] nums, int[][] expected)
    {
        Rotate(nums);
        Assert.Equal(expected, nums);
    }
}