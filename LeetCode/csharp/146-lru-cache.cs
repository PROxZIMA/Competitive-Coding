using System.Collections;
using System.Text;
using Newtonsoft.Json;

namespace SDE_Sheet;

public class P146
{
    public class LRUCache
    {
        private readonly int _capacity;
        public readonly Dictionary<int, (LinkedListNode<int> node, int value)> _hash;
        private readonly LinkedList<int> _list;
        public LRUCache(int capacity)
        {
            _capacity = capacity;
            _hash = [];
            _list = [];
        }

        private void InsertAtBegining(int key, int value)
        {
            var node = _list.AddFirst(key);
            _hash[key] = (node, value);
        }

        private void Remove(int key)
        {
            if (_hash.TryGetValue(key, out var node))
            {
                _list.Remove(node.node);
                _hash.Remove(key);
            }
        }

        private void Prioritize(int key, int value)
        {
            Remove(key);
            InsertAtBegining(key, value);
        }

        public int Get(int key)
        {
            if (_hash.TryGetValue(key, out var node))
            {
                Prioritize(key, node.value);
                return node.value;
            }

            return -1;
        }

        public void Put(int key, int value)
        {
            if (_hash.TryGetValue(key, out var _))
            {
                Prioritize(key, value);
                return;
            }
            else if (_list.Count == _capacity)
            {
                if (_list.Last is not null) _hash.Remove(_list.Last.Value);
                _list.RemoveLast();
            }
            InsertAtBegining(key, value);
        }

        public override string ToString()
        {
            return string.Join(", ", _list.Select(i => $"{i}({_hash[i].value})"));
        }
    }

    public class TestData : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[]
            {
            new string[] { "LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get" },
            new int[][] { [2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4] },
            new int?[] { null, null, null, 1, null, -1, null, -1, 3, 4}
            };

            yield return new object[]
            {
            new string[] { "LRUCache","put","put","get","put","get","put","get","get","get" },
            new int[][] { [2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4] },
            new int?[] { null,null,null,0,null,-1,null,-1,3,4 }
            };

            yield return new object[]
            {
            new string[] { "LRUCache", "put", "get" },
            new int[][] { [1], [2, 1], [2] },
            new int?[] { null, null, 1}
            };
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }

    [Theory]
    [ClassData(typeof(TestData))]
    public void Test1(string[] operations, int[][] inputs, int?[] outputs)
    {
        LRUCache lRUCache = new(0);
        for (int i = 0; i < operations.Length; i++)
        {
            var input = inputs[i];
            switch (operations[i])
            {
                case "LRUCache":
                    lRUCache = new LRUCache(input[0]);
                    break;
                case "put":
                    lRUCache.Put(input[0], input[1]);
                    break;
                case "get":
                    Assert.Equal(outputs[i], lRUCache.Get(input[0]));
                    break;
                default:
                    break;

            }
            Console.WriteLine($"[{operations[i]} ({JsonConvert.SerializeObject(input)})] cache:{lRUCache}, expected: {outputs[i]}");
        }
    }
}