package com.headstrong.app;

import java.util.Arrays;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;


public class EgRowTest extends TestCase {

    public EgRowTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(EgRowTest.class);
    }

    private EgRow buildTestRow() {
        return new EgRow(
            Arrays.asList("col1", "col2"),
            new EgCell((long)1, false),
            new EgCell("msg1", false)
        );
    }

    public void testGetLongAtIndex() {
        EgRow row = buildTestRow();
        assertEquals(1, row.getLong(0));
    }

    public void testGetStringAtIndex() {
        EgRow row = buildTestRow();
        assertEquals("msg1", row.getString(1));
    }

    public void testGetLongForColumnName() {
        EgRow row = buildTestRow();
        assertEquals(1, row.getLong("col1"));
    }

    public void testGetStringForColumnName() {
        EgRow row = buildTestRow();
        assertEquals("msg1", row.getString("col2"));
    }

}
