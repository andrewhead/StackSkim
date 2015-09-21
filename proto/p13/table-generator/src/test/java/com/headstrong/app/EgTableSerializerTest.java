package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;


public class EgTableSerializerTest extends TestCase {

    public EgTableSerializerTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(EgTableSerializerTest.class);
    }

    public void testSerializeTable() {
        List<String> columnNames = Arrays.asList("col1", "col2");
        EgTable table = new EgTable(columnNames, Arrays.asList(ColumnType.LONG, ColumnType.STRING));
        table.addRow(new EgRow(columnNames, new EgCell(1, true), new EgCell("msg1", false)));
        table.addRow(new EgRow(columnNames, new EgCell(2, false), new EgCell("msg2", true)));
        Gson gson = new GsonBuilder()
            .registerTypeAdapter(EgTable.class, new EgTableSerializer())
            .registerTypeAdapter(EgRow.class, new EgRowSerializer())
            .registerTypeAdapter(EgCell.class, new EgCellSerializer())
            .create();
        String json = gson.toJson(table);
        assertEquals("{" +
            "\"columnNames\":[\"col1\",\"col2\"]," +
            "\"columnTypes\":[\"LONG\",\"STRING\"]," +
            "\"rows\":[" +
                "[{\"data\":1,\"satisfies\":true},{\"data\":\"msg1\",\"satisfies\":false}]," +
                "[{\"data\":2,\"satisfies\":false},{\"data\":\"msg2\",\"satisfies\":true}]" +
            "]}",
            json);
    }

}
