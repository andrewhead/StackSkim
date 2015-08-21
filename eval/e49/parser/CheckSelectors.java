import parser.gen.*;
import parser.*;

import java.util.ArrayList;
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;


public class CheckSelectors {

    public static void main(String[] args) throws Exception {

        FileReader fileReader = new FileReader(args[0]);
        BufferedReader bufferedReader = new BufferedReader(fileReader);
        String line;

        ArrayList<String> successStrings = new ArrayList<String>();
        ArrayList<String> failureStrings = new ArrayList<String>();
        ArrayList<String> failureMessages = new ArrayList<String>();
        int successCount = 0;
        int totalCount = 0;

        // Process each line of the input file as a separate CSS selector to be parsed
        while (true) {
            line = bufferedReader.readLine();
            if (line == null) {
                break;
            }
            try {
                parseString(line);
                successCount += 1;
                successStrings.add(line);
            } catch (RuntimeException e) {
                failureStrings.add(line);
                failureMessages.add(e.toString());
            }
            totalCount += 1;
        }

        float successRate = (successCount / (float) totalCount) * 100;
        System.out.printf("Success rate: %.2f%% (%d/%d)\n",
            successRate, successCount, totalCount);
        System.out.println();
        System.out.println("Strings that failed to parse:");
        for (String string : failureStrings) {
            System.out.println(string);
        }
        System.out.println();

        System.out.println("Reasons for failures:");
        for (int i = 0; i < failureStrings.size(); i++) {
            System.out.printf("* %s: %s\n", failureStrings.get(i), failureMessages.get(i));
            System.out.println((int)failureStrings.get(i).charAt(13));
        }
        System.out.println();

    }

    public static void parseString(String string) throws IOException {

        // Prepare input stream
        InputStream stream = new ByteArrayInputStream(string.getBytes(StandardCharsets.UTF_8));
        ANTLRInputStream input = new ANTLRInputStream(stream);

        // Create a lexer that exits at the first lexical error
        ExitingCssLexer lexer = new ExitingCssLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // Create default parser
        CssParser parser = new CssParser(tokens);

        // Disable default logging of exceptions
        lexer.removeErrorListeners();
        parser.removeErrorListeners();

        // Prepare parser to propagate exception on parse error
        parser.setErrorHandler(new ExitErrorStrategy());

        // Parse the example!
        ParseTree tree = parser.selector();

    }

}
