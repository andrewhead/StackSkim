import org.antlr.v4.runtime.*;
import parser.gen.*;


public class ExitingCssLexer extends CssLexer {

    public ExitingCssLexer(CharStream input) {
        super(input);
    }

    public void recover(LexerNoViableAltException e) {
        throw new RuntimeException(e);
    }

}

