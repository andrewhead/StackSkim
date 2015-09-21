package com.headstrong.app;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;


public class EgTableTest extends TestCase {

    public EgTableTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(EgTableTest.class);
    }

    public void testAddRows() {
        List<String> columnNames = Arrays.asList("col1", "col2");
        List<ColumnType> columnTypes = Arrays.asList(ColumnType.LONG, ColumnType.STRING);
        EgTable table = new EgTable(columnNames, columnTypes);
        table.addRow(new EgRow(columnNames, 1, "msg1"));
        table.addRow(new EgRow(columnNames, 2, "msg2"));
        assertEquals(Arrays.asList(1, "msg1"), table.getRow(0).getCells());
        assertEquals(Arrays.asList(2, "msg2"), table.getRow(1).getCells());
    }

}
