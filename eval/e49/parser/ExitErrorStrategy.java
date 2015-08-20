import org.antlr.v4.runtime.*;

/**
 * REUSE: This code is adapted from
 * The Definitive ANTLR4 Reference v2.0
 * Chapter 9, page 174
 */
public class ExitErrorStrategy extends DefaultErrorStrategy {

    @Override
    public void recover(Parser recognizer, RecognitionException e) {
        throw new RuntimeException(e);
    }

    @Override
    public Token recoverInline(Parser recognizer) {
        throw new RuntimeException(new InputMismatchException(recognizer));
    }

    @Override
    public void sync(Parser recognizer) {}

}
