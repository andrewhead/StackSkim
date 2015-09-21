package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.util.ArrayList;
import net.sf.jsqlparser.statement.Statement;


public class ExpressionExtractorTest extends TestCase {

    public ExpressionExtractorTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(ExpressionExtractorTest.class);
    }

    public void testNoCrashWithNoWhereCondition() {
        Statement stmt = TestJsqlParser.parse("SELECT col1 FROM tbl");
        SelectExpressionExtractor expExtractor = new SelectExpressionExtractor();
        EgExpression root = expExtractor.visit(stmt);
    }

    public void testExtractSingleExpression() {
        Statement stmt = TestJsqlParser.parse("SELECT col1 FROM tbl WHERE col1 = 0");
        SelectExpressionExtractor expExtractor = new SelectExpressionExtractor();
        EgExpression root = expExtractor.visit(stmt);
        assertEquals("col1 = 0", root.toString());
        assertEquals(0, root.getChildren().size());
    }

    public void testExtractAndTest() {
        Statement stmt = TestJsqlParser.parse("SELECT col1, col2 FROM tbl WHERE col1 = 0 AND col2 = 0");
        SelectExpressionExtractor expExtractor = new SelectExpressionExtractor();
        EgExpression root = expExtractor.visit(stmt);
        assertEquals(root.getChildren().size(), 2);
        EgExpression left = root.getChildren().get(0);
        assertEquals("col1 = 0", left.toString());
        EgExpression right = root.getChildren().get(1);
        assertEquals("col2 = 0", right.toString());
    }

    public void testGetLeafExpressions() {
        Statement stmt = TestJsqlParser.parse("SELECT col1, col2 FROM tbl WHERE col1 = 0 AND col2 = 0");
        SelectExpressionExtractor expExtractor = new SelectExpressionExtractor();
        expExtractor.visit(stmt);
        ArrayList<EgExpression> leaves = expExtractor.getLeafExpressions();
        assertEquals(2, leaves.size());
    }

}
