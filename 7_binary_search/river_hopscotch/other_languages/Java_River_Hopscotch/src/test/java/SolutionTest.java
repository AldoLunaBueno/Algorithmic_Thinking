import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.*;
import java.util.stream.Stream;

class SolutionTest {
    @ParameterizedTest
    @MethodSource("testMain")
    void testMain(String input, String expected) throws Exception {
        provideInput(input);
        OutputStream out = receiveOutput();
        Main.main(null);
        String actual = out.toString();
        assertEquals(expected, actual);
    }
    static Stream<Arguments> testMain() {
        String nl = System.lineSeparator();
        return Stream.of(
                Arguments.of("12 2 1\n5\n8\n", "5" + nl),
                Arguments.of("12 4 2\n1\n3\n8\n9\n", "3" + nl),
                Arguments.of("25 5 2\n2\n14\n11\n21\n17\n", "4" + nl),
                Arguments.of("12 4 2\n2\n4\n5\n8\n", "4" + nl)
        );
    }
    private void provideInput(String data) {
        ByteArrayInputStream testIn = new ByteArrayInputStream(data.getBytes());
        System.setIn(testIn);
    }
    private OutputStream receiveOutput() {
        OutputStream stdout = new ByteArrayOutputStream();
        System.setOut(new PrintStream(stdout));
        return stdout;
    }
}