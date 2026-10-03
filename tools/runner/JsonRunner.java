import org.junit.runner.*;
import org.junit.runner.notification.*;
import java.util.*;

/** Runs one JUnit 4 class and prints one JSON line per test method: {"method":..,"status":pass|fail|ignored,"message":..}. */
public class JsonRunner {
    public static void main(String[] args) throws Exception {
        Class<?> c = Class.forName(args[0]);
        JUnitCore core = new JUnitCore();
        final Set<String> failed = new HashSet<>();
        core.addListener(new RunListener() {
            @Override public void testFailure(Failure f) {
                failed.add(f.getDescription().getMethodName());
                System.out.println("{\"method\":" + q(f.getDescription().getMethodName())
                    + ",\"status\":\"fail\",\"message\":" + q(String.valueOf(f.getMessage()))
                    + ",\"exception\":" + q(f.getException().getClass().getName()) + "}");
            }
            @Override public void testAssumptionFailure(Failure f) { testFailure(f); }
            @Override public void testIgnored(Description d) {
                System.out.println("{\"method\":" + q(d.getMethodName()) + ",\"status\":\"ignored\"}");
            }
            @Override public void testFinished(Description d) {
                if (!failed.contains(d.getMethodName()))
                    System.out.println("{\"method\":" + q(d.getMethodName()) + ",\"status\":\"pass\"}");
            }
        });
        Result r = core.run(c);
        System.out.println("{\"summary\":{\"run\":" + r.getRunCount() + ",\"failures\":" + r.getFailureCount()
            + ",\"ignored\":" + r.getIgnoreCount() + ",\"ms\":" + r.getRunTime() + "}}");
        System.exit(0);
    }
    static String q(String s) {
        if (s == null) return "null";
        StringBuilder b = new StringBuilder("\"");
        for (char ch : s.toCharArray()) {
            if (ch == '"' || ch == '\\') b.append('\\').append(ch);
            else if (ch == '\n') b.append("\\n"); else if (ch == '\r') b.append("\\r"); else if (ch == '\t') b.append("\\t");
            else if (ch < 0x20) b.append(String.format("\\u%04x", (int) ch)); else b.append(ch);
        }
        return b.append('"').toString();
    }
}
