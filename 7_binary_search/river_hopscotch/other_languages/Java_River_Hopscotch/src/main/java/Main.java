import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int L, n, m_removes;
    static Integer[] rocks;
    public static void main(String[] args) throws Exception {
        getData();
        solve();
    }

    private static void solve() throws Exception {
        Arrays.sort(rocks);
        int result = discreteBisectionMethod(0, L);
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
    private static int booleanToInt(boolean b) {
        return b ? 1 : -1;
    }

    private static int discreteBisectionMethod(int low, int high) throws Exception {
        if (booleanToInt(canMakeMinJump(low)) * booleanToInt(canMakeMinJump(high)) > 0) {
            throw new Exception("Bad boundary");
        }
        while (high - low > 1) {
            int center = (high + low) / 2;
            if (booleanToInt(canMakeMinJump(low)) * booleanToInt(canMakeMinJump(center)) < 0) {
                high = center;
            } else if (booleanToInt(canMakeMinJump(center)) * booleanToInt(canMakeMinJump(high)) < 0) {
                low = center;
            } else if (booleanToInt(canMakeMinJump(center)) == 0) {
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
        n += 2; // rocks[0] and rocks[L] added
        scanner.close();
    }
}
