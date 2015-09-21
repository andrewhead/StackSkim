package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;

import net.sf.jsqlparser.statement.Statement;
import java.util.ArrayList;


public class ColumnTypeFinderTest extends TestCase {

    public ColumnTypeFinderTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(ColumnTypeFinderTest.class);
    }

    private ArrayList<EgExpression> getExpressions(String sql) {
        Statement stmt = TestJsqlParser.parse(sql);
        SelectExpressionExtractor selExtractor = new SelectExpressionExtractor();
        selExtractor.visit(stmt);
        return selExtractor.getLeafExpressions();
    }

    public void testFindLongColumnType() {
        ColumnTypeFinder colTypeFinder = new ColumnTypeFinder();
        ArrayList<EgExpression> expressions = getExpressions(
            "SELECT col1 FROM tbl WHERE col1 = 2;");
        ColumnType colType = colTypeFinder.getType("col1", expressions);
        assertEquals(ColumnType.LONG, colType);
    }

    public void testFindStringColumnType() {
        ColumnTypeFinder colTypeFinder = new ColumnTypeFinder();
        ArrayList<EgExpression> expressions = getExpressions(
            "SELECT col1 FROM tbl WHERE col1 = 'msg';");
        ColumnType colType = colTypeFinder.getType("col1", expressions);
        assertEquals(ColumnType.STRING, colType);
    }

    public void testGetNoTypeIfColumnNotInExpression() {
        ColumnTypeFinder colTypeFinder = new ColumnTypeFinder();
        ArrayList<EgExpression> expressions = getExpressions("SELECT col1 FROM tbl");
        ColumnType colType = colTypeFinder.getType("col1", expressions);
        assertEquals(null, colType);
    }

    public void testGetNoTypeIfConflictingTypesFoundInExpressions() {
        ColumnTypeFinder colTypeFinder = new ColumnTypeFinder();
        ArrayList<EgExpression> expressions = getExpressions(
            "SELECT col1 FROM tbl WHERE col1 > 2 AND col1 = 'msg';");
        ColumnType colType = colTypeFinder.getType("col1", expressions);
        assertEquals(null, colType);
    }

    public void testNoMistakeOneColumnsTypeForAnothers() {
        ColumnTypeFinder colTypeFinder = new ColumnTypeFinder();
        ArrayList<EgExpression> expressions = getExpressions(
            "SELECT col1 FROM tbl WHERE col2 = 'msg';");
        ColumnType colType = colTypeFinder.getType("col1", expressions);
        assertEquals(null, colType);
    }

}
