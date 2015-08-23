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


public class PrintTrees {

    public static void main(String[] args) throws Exception {

        FileReader fileReader = new FileReader(args[0]);
        BufferedReader bufferedReader = new BufferedReader(fileReader);
        String line, selector;

        // Process each line of the input file as a separate CSS selector to be parsed
        while (true) {
            line = bufferedReader.readLine();
            if (line == null) {
                break;
            }
            selector = line.split(",,,")[0];
            try {
                printParseTree(selector);
            } catch (RuntimeException e) {
            }
        }

    }

    public static void printParseTree(String string) throws IOException {

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
        System.out.println(tree.toStringTree(parser));

    }

}
