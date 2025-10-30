using System.Collections;

namespace SDE_Sheet;

public class P121
{
    private static int Solution(int[] prices)
    {
        var profit = 0;
        var lowestBuy = prices[0];
        for (var i = 1; i < prices.Length; i++)
        {
            if (prices[i] < lowestBuy)
            {
                lowestBuy = prices[i];
            }
            else if (prices[i] - lowestBuy > profit)
            {
                profit = prices[i] - lowestBuy;
            }
        }
        return profit;
    }

    private static int SolutionN(int[] prices)
    {
        var maxTillIFromBehind = new int[prices.Length];
        maxTillIFromBehind[^1] = prices[^1];

        for (var i = prices.Length - 2; i >= 0; i--)
        {
            maxTillIFromBehind[i] = Math.Max(maxTillIFromBehind[i + 1], prices[i]);
        }

        var profit = 0;
        for (var i = 0; i < prices.Length; i++)
        {
            profit = Math.Max(profit, maxTillIFromBehind[i] - prices[i]);
        }
        return profit;
    }

    private static int SolutionN2(int[] prices)
    {
        var profit = 0;
        for (var i = 0; i < prices.Length; i++)
        {
            for (var j = i + 1; j < prices.Length; j++)
            {
                profit = Math.Max(profit, prices[j] - prices[i]);
            }
        }
        return profit;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new int[] { 7,1,5,3,6,4 },
            5
            };

            yield return new object[]
            {
            new int[] { 7,6,4,3,1 },
            0
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(int[] prices, int expected)
    {
        Assert.Equal(expected, Solution(prices));
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test2(int[] prices, int expected)
    {
        Assert.Equal(expected, SolutionN(prices));
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test3(int[] prices, int expected)
    {
        Assert.Equal(expected, SolutionN2(prices));
    }
}