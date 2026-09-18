public class Solution {
    public int[] ReplaceElements(int[] arr) {
        if (arr.Length == 1)
        {
            return [-1];
        }
        int[] maxes = new int[arr.Length];

        maxes[^1] = -1;
        maxes[^2] = arr[^1];

        for (int i = arr.Length - 2; i > 0 ; i--)
        {
            maxes[i-1] = Math.Max(arr[i], maxes[i]);
        }

        return maxes;
    }
}