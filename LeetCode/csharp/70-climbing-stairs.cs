using System.Collections;

namespace SDE_Sheet;

public class P70
{
    public int[] fibo;
    public P70()
    {
        var limit = 46;
        fibo = new int[limit];
        fibo[0] = 1;
        fibo[1] = 1;
        for (int i = 2; i < limit; i++)
        {
            fibo[i] = fibo[i - 1] + fibo[i - 2];
        }
    }
    private int ClimbStairs(int n)
    {
        return fibo[n];
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            1,
            1
            };

            yield return new object[]
            {
            2,
            2
            };

            yield return new object[]
            {
            3,
            3
            };

            yield return new object[]
            {
            4,
            5
            };

            yield return new object[]
            {
            5,
            8
            };

            yield return new object[]
            {
            6,
            13
            };

            yield return new object[]
            {
            45,
            1836311903
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int nums, int expected)
    {
        Assert.Equal(expected, ClimbStairs(nums));
    }
}