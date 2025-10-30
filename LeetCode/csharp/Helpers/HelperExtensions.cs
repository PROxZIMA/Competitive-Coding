namespace SDE_Sheet.Helpers;

public static class HelperExtensions
{
    public static bool SequenceEquals<T>(this T[,] a, T[,] b) =>
        a.Rank == b.Rank &&
        Enumerable.Range(0, a.Rank).All(d => a.GetLength(d) == b.GetLength(d)) &&
        a.Cast<T>().SequenceEqual(b.Cast<T>());

    public static bool SequenceEquals(this IEnumerable<int> a, IEnumerable<int> b) =>
        a.SequenceEqual(b);

    public static bool SequenceEquals(this IEnumerable<IEnumerable<int>> a, IEnumerable<IEnumerable<int>> b) =>
        a.Count() == b.Count() &&
        a.Zip(b, (innerA, innerB) => innerA.SequenceEqual(innerB)).All(result => result);

    public static bool SequenceEquals(this int[] a, int[] b) =>
        a.SequenceEqual(b);

    public static bool SequenceEquals(this int[][] a, int[][] b) =>
        a.Length == b.Length &&
        a.Zip(b, (rowA, rowB) => rowA.SequenceEqual(rowB)).All(result => result);
}