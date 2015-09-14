package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;

import java.util.ArrayList;
import net.sf.jsqlparser.statement.Statement;


public class DataGeneratorTest extends TestCase {

    public DataGeneratorTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(DataGeneratorTest.class);
    }

    private ArrayList<EgExpression> getExpressionsForSql(String sql) {
        Statement stmt = TestJsqlParser.parse(sql);
        SelectExpressionExtractor selExtractor = new SelectExpressionExtractor();
        selExtractor.visit(stmt);
        return selExtractor.getLeafExpressions();
    }
    
    private Object getDataForFirstExpression(String sql, boolean satisfying) {
        ArrayList<EgExpression> expressions = getExpressionsForSql(sql);
        DataGenerator dataGenerator = new DataGenerator(satisfying);
        expressions.get(0).accept(dataGenerator);
        return dataGenerator.getData();
    }

    private Object getTrueDataForFirstExpression(String sql) {
        return getDataForFirstExpression(sql, true);
    }

    private Object getFalseDataForFirstExpression(String sql) {
        return getDataForFirstExpression(sql, false);
    }

    public void testGenerateStringEquality() {
        Object data = getTrueDataForFirstExpression("SELECT * FROM tbl WHERE col1 = 'msg'");
        assertTrue(data instanceof String);
        assertEquals("msg", (String)data);
    }

    public void testGenerateStringEqualityIfEqualityBackwards() {
        Object data = getTrueDataForFirstExpression("SELECT * FROM tbl WHERE 'msg' = col1");
        assertEquals("msg", (String)data);
    }

    public void testGenerateLongIntegerEquality() {
        Object data = getTrueDataForFirstExpression("SELECT * FROM tbl WHERE col1 = 2");
        assertTrue(data instanceof Long);
        assertEquals(2, ((Long)data).intValue());
    }

    public void testGenerateLongIntegerInequality() {
        Object data = getFalseDataForFirstExpression("SELECT * FROM tbl WHERE col1 = 2");
        assertTrue(data instanceof Long);
        assertNotEquals(2, ((Long)data).longValue());
    }

    public void testGenerateGreaterThanInteger() {
        Object data = getFalseDataForFirstExpression("SELECT * FROM tbl WHERE col1 > 2");
        assertTrue(((Long)data).longValue() > 2);
    }

    public void testGenerateGreaterThanIntegerReverseArgumentOrder() {
        Object data = getFalseDataForFirstExpression("SELECT * FROM tbl WHERE 2 < col1");
        assertTrue(((Long)data).longValue() > 2);
    }

}
