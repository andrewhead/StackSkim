package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;

import java.util.ArrayList;
import net.sf.jsqlparser.statement.Statement;
import net.sf.jsqlparser.expression.Expression;
import net.sf.jsqlparser.expression.BinaryExpression;
import net.sf.jsqlparser.expression.LongValue;


public class DataExtractorTest extends TestCase {

    public DataExtractorTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(DataExtractorTest.class);
    }

    private Expression getFirstJsqlExpression(String sql) {
        Statement stmt = TestJsqlParser.parse(sql);
        SelectExpressionExtractor selExtractor = new SelectExpressionExtractor();
        selExtractor.visit(stmt);
        ArrayList<EgExpression> expressions = selExtractor.getLeafExpressions();
        return expressions.get(0).getJsqlParserExpression();
    }

    public void testFindDataAsLeftArgument() {
        BinaryExpression exp = (BinaryExpression) 
            getFirstJsqlExpression("SELECT col1 FROM tbl WHERE 2 = col1;");
        DataExtractor dataExtractor = new DataExtractor();
        DataPosition pos = dataExtractor.getDataPosition(exp);
        assertEquals(DataPosition.LEFT, pos);
    }

    public void testFindDataAsRightArgument() {
        BinaryExpression exp = (BinaryExpression) 
            getFirstJsqlExpression("SELECT col1 FROM tbl WHERE col1 = 2;");
        DataExtractor dataExtractor = new DataExtractor();
        DataPosition pos = dataExtractor.getDataPosition(exp);
        assertEquals(DataPosition.RIGHT, pos);
    }

    public void testNoDataPositionIfBothColumns() {
        BinaryExpression exp = (BinaryExpression) 
            getFirstJsqlExpression("SELECT col1 FROM tbl WHERE col1 = col2;");
        DataExtractor dataExtractor = new DataExtractor();
        DataPosition pos = dataExtractor.getDataPosition(exp);
        assertEquals(DataPosition.NONE, pos);
    }

    public void testNoDataPositionIfBothAreData() {
        BinaryExpression exp = (BinaryExpression) 
            getFirstJsqlExpression("SELECT col1 FROM tbl WHERE 2 = 2;");
        DataExtractor dataExtractor = new DataExtractor();
        DataPosition pos = dataExtractor.getDataPosition(exp);
        assertEquals(DataPosition.NONE, pos);
    }

    public void testExtractDataFromRightArgument() {
        BinaryExpression exp = (BinaryExpression) 
            getFirstJsqlExpression("SELECT col1 FROM tbl WHERE col1 = 2;");
        DataExtractor dataExtractor = new DataExtractor();
        Object data = dataExtractor.extractData(exp);
        assertTrue(data instanceof Long);
        assertTrue(((Long)data).longValue() == 2);
    }

    public void testExtractDataFromLeftArgument() {
        BinaryExpression exp = (BinaryExpression) 
            getFirstJsqlExpression("SELECT col1 FROM tbl WHERE 2 = col1;");
        DataExtractor dataExtractor = new DataExtractor();
        Object data = dataExtractor.extractData(exp);
        assertTrue(data instanceof Long);
        assertTrue(((Long)data).longValue() == 2);
    }

}
