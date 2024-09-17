import java.util.Arrays;
import java.util.Scanner;
import java.util.concurrent.Callable;
import java.util.function.Function;

public class Solution {
    static int L, n, m_removes;
    static Integer[] rocks;
    static final int MAX_RIVER_WIDTH = 1_000_000_000;
    public static void main(String[] args) throws Exception {
        getData();
        solve();
    }

    private static void solve() throws Exception {
        Arrays.sort(rocks);
        Function<Integer, Integer> f = x -> canMakeMinJump(x) ? 1 : -1;
        int result = discreteBisectionMethod(f, 0, L);
        System.out.println(result);
    }

    private static boolean canMakeMinJump(Integer jumpGuess) {
        int base = 0, next = 1;
        int elimination_count = 0;
        while (next < n) {
            while (next < n
                    && rocks[next] - rocks[base] < jumpGuess) {
                elimination_count++;
                next++;
            }
            base = next;
            next = base + 1;
        }
        return elimination_count <= m_removes; // feasibility
    }

    private static int discreteBisectionMethod(
            Function<Integer, Integer> f, int low, int high)
            throws Exception {
        if (f.apply(low) * f.apply(high) > 0) {
            throw new Exception("Bad boundary");
        }
        while (high - low > 1) {
            int center = (high + low) / 2;
            if (f.apply(low) * f.apply(center) < 0) {
                high = center;
            } else if (f.apply(center) * f.apply(high) < 0) {
                low = center;
            } else if (f.apply(center) == 0) {
                return center;
            }
        }
        return low;
    }

    private static void getData() {
        Scanner scanner = new Scanner(System.in);
        L = scanner.nextInt();
        n = scanner.nextInt();
        m_removes = scanner.nextInt();

        rocks = new Integer[n+2];
        rocks[0] = 0;
        for(int i=1; i<n+1; i++) {
            int rock = scanner.nextInt();
            rocks[i] = rock;
        }
        rocks[n+1] = L;
        scanner.close();
    }
}
