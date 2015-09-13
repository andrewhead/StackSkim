package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.util.ArrayList;
import net.sf.jsqlparser.statement.Statement;


public class ColumnExtractorTest extends TestCase {

    public ColumnExtractorTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(ColumnExtractorTest.class);
    }

    public void testExtractSingleColumnName() {
        Statement stmt = TestJsqlParser.parse("SELECT col1 FROM tbl");
        SelectColumnExtractor columnExtractor = new SelectColumnExtractor();
        ArrayList<String> colNames = columnExtractor.getColumnNames(stmt);
        assertEquals(1, colNames.size());
        assertEquals("col1", colNames.get(0));
    }

    public void testExtractMultipleColumnNames() {
        Statement stmt = TestJsqlParser.parse("SELECT col1, col2 FROM tbl");
        SelectColumnExtractor columnExtractor = new SelectColumnExtractor();
        ArrayList<String> colNames = columnExtractor.getColumnNames(stmt);
        assertEquals(2, colNames.size());
        assertTrue(colNames.contains("col1"));
        assertTrue(colNames.contains("col2"));
    }

}
