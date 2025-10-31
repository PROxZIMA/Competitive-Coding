using System.Collections;

namespace SDE_Sheet;

public class P2
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int val = -1, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }

        public override string ToString()
        {
            if (next is null)
                return $"{val}";
            return $"{val}, {next}";
        }
    }

    private static ListNode Solution(ListNode l1, ListNode l2)
    {
        ListNode r1 = new();
        ListNode curr = r1;
        const int divisor = 10;
        int quotient = 0;
        while (l1 is not null || l2 is not null)
        {
            var dividend = (l1 is not null ? l1.val : 0) +
                           (l2 is not null ? l2.val : 0) +
                           quotient;

            curr.val = dividend % divisor;
            quotient = dividend / divisor;

            if (l1?.next is not null || l2?.next is not null)
            {
                ListNode next = new();
                curr.next = next;
                curr = next;
            }

            if (l1 is not null)
                l1 = l1.next;
            if (l2 is not null)
                l2 = l2.next;
        }

        if (quotient != 0)
        {
            curr.next = new(quotient);
        }
        return r1;
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            ListNode a1 = new(2, new(4, new(3)));
            ListNode b1 = new(5, new(6, new(4)));
            ListNode r1 = new(7, new(0, new(8)));
            yield return new object[]
            {
            a1,
            b1,
            r1
            };

            ListNode c1 = new(0);
            ListNode d1 = new(0);
            ListNode s1 = new(0);
            yield return new object[]
            {
            c1,
            d1,
            s1
            };

            ListNode e1 = new(9, new(9, new(9, new(9, new(9, new(9, new(9)))))));
            ListNode f1 = new(9, new(9, new(9, new(9))));
            ListNode t1 = new(8, new(9, new(9, new(9, new(0, new(0, new(0, new(1))))))));
            yield return new object[]
            {
            e1,
            f1,
            t1
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(ListNode l1, ListNode l2, ListNode expected)
    {
        var result = Solution(l1, l2);
        Console.WriteLine(result);
        Assert.Equivalent(expected, result);
        // while (expected.next is not null)
        // {
        //     Assert.Equal(expected.val, result.val);
        //     expected = expected.next;
        //     result = result.next;
        // }
    }
}