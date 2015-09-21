package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;

import net.sf.jsqlparser.statement.Statement;


public class ColumnNameFinderTest extends TestCase {

    public ColumnNameFinderTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(ColumnNameFinderTest.class);
    }

    private EgExpression getFirstExpressionFromSQL(String sql) {
        Statement stmt = TestJsqlParser.parse(sql);
        SelectExpressionExtractor selExtractor = new SelectExpressionExtractor();
        selExtractor.visit(stmt);
        return selExtractor.getLeafExpressions().get(0);
    }

    public void testFindColumnNameAsLeftArgument() {
        EgExpression expr = getFirstExpressionFromSQL("SELECT col1 FROM tbl WHERE col1 > 2");
        ColumnNameFinder nameFinder = new ColumnNameFinder();
        String name = nameFinder.getName(expr.getJsqlParserExpression());
        assertEquals("col1", name);
    }

    public void testFindColumnNameAsRightArgument() {
        EgExpression expr = getFirstExpressionFromSQL("SELECT col1 FROM tbl WHERE 2 > col1");
        ColumnNameFinder nameFinder = new ColumnNameFinder();
        String name = nameFinder.getName(expr.getJsqlParserExpression());
        assertEquals("col1", name);
    }

}
