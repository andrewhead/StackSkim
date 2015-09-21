package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;

import com.google.gson.GsonBuilder;
import com.google.gson.Gson;


public class EgCellSerializerTest extends TestCase {

    public EgCellSerializerTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(EgCellSerializerTest.class);
    }

    public void testSerializeCell() {
        Gson gson = new GsonBuilder()
            .registerTypeAdapter(EgCell.class, new EgCellSerializer())
            .create();
        String json = gson.toJson(new EgCell(1, false));
        assertEquals("{\"data\":1,\"satisfies\":false}", json);
    }

}
