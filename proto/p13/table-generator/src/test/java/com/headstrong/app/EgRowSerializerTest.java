package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;

import java.util.Arrays;

import com.google.gson.GsonBuilder;
import com.google.gson.Gson;


public class EgRowSerializerTest extends TestCase {

    public EgRowSerializerTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(EgRowSerializerTest.class);
    }

    public void testSerializeRow() {
        EgRow row = new EgRow(Arrays.asList("col1", "col2"),
            new EgCell(1, true), new EgCell("msg1", false));
        Gson gson = new GsonBuilder()
            .registerTypeAdapter(EgRow.class, new EgRowSerializer())
            .registerTypeAdapter(EgCell.class, new EgCellSerializer())
            .create();
        assertEquals(
            "[{\"data\":1,\"satisfies\":true},{\"data\":\"msg1\",\"satisfies\":false}]",
            gson.toJson(row));
    }

}
