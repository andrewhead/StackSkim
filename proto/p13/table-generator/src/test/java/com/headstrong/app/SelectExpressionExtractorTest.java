package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.util.ArrayList;
import net.sf.jsqlparser.statement.Statement;


public class SelectExpressionExtractorTest extends TestCase {

    public SelectExpressionExtractorTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(SelectExpressionExtractorTest.class);
    }

    private EgExpression extractRootExpression(String sql) {
        Statement stmt = TestJsqlParser.parse(sql);
        SelectExpressionExtractor expExtractor = new SelectExpressionExtractor();
        return expExtractor.visit(stmt);
    }

    public void testNoCrashWithNoWhereCondition() {
        extractRootExpression("SELECT col1 FROM tbl");
    }

    public void testExtractSingleExpression() {
        EgExpression root = extractRootExpression("SELECT col1 FROM tbl WHERE col1 = 0");
        assertEquals("col1 = 0", root.toString());
        assertEquals(0, root.getChildren().size());
    }

    public void testExtractAndTest() {
        EgExpression root = extractRootExpression(
            "SELECT col1, col2 FROM tbl WHERE col1 = 0 AND col2 = 0");
        assertTrue(root instanceof EgAndExpression);
        assertEquals(2, root.getChildren().size());
        EgExpression left = root.getChildren().get(0);
        assertEquals("col1 = 0", left.toString());
        EgExpression right = root.getChildren().get(1);
        assertEquals("col2 = 0", right.toString());
    }

    public void testExtractOrTest() {
        EgExpression root = extractRootExpression(
            "SELECT col1, col2 FROM tbl WHERE col1 = 0 OR col2 = 0");
        assertTrue(root instanceof EgOrExpression);
        assertEquals(2, root.getChildren().size());
    }

    public void testAssociateRightToLeft() {
        // Parsing the WHERE conditions here, we see a parse tree like:
        // ((col1 = 0 OP col2 = 0) OP col3 = 0)
        // Where the left child of the root has 2 children
        // This test makes sure that that behavior is maintained in JSqlParser
        EgExpression andRoot = extractRootExpression(
            "SELECT * FROM tbl WHERE col1 = 0 AND col2 = 0 AND col3 = 0");
        assertEquals(2, andRoot.getChildren().get(0).getChildren().size());
        EgExpression orRoot = extractRootExpression(
            "SELECT * FROM tbl WHERE col1 = 0 OR col2 = 0 OR col3 = 0");
        assertEquals(2, orRoot.getChildren().get(0).getChildren().size());
    }

    public void testAndPrecedenceHigherThanOr() {
        EgExpression root;
        root = extractRootExpression("SELECT * FROM tbl WHERE col1 = 0 AND col2 = 0 OR col3 = 0");
        assertTrue(root instanceof EgOrExpression);
        root = extractRootExpression("SELECT * FROM tbl WHERE col1 = 0 OR col2 = 0 AND col3 = 0");
        assertTrue(root instanceof EgOrExpression);
    }

    public void testParenthesesIncreasePrecedenceOfOperator() {
        EgExpression root;
        root = extractRootExpression("SELECT * FROM tbl WHERE col1 = 0 AND (col2 = 0 OR col3 = 0)");
        assertTrue(root instanceof EgAndExpression);
    }

    public void testParenthesesSimplifyToExpressionInside() {
        EgExpression root;
        root = extractRootExpression("SELECT * FROM tbl WHERE (col1 = 0 OR col2 = 0)");
        assertTrue(root instanceof EgOrExpression);
        root = extractRootExpression("SELECT * FROM tbl WHERE co1 = 0 AND (col2 = 0 OR col3 = 0)");
        assertTrue(root.getChildren().get(1) instanceof EgOrExpression);
    }

    public void testGetLeafExpressions() {
        Statement stmt = TestJsqlParser.parse(
            "SELECT col1, col2 FROM tbl WHERE col1 = 0 AND col2 = 0");
        SelectExpressionExtractor expExtractor = new SelectExpressionExtractor();
        expExtractor.visit(stmt);
        ArrayList<EgExpression> leaves = expExtractor.getLeafExpressions();
        assertEquals(2, leaves.size());
    }

}
