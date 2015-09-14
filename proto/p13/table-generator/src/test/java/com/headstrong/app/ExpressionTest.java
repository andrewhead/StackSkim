package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.util.ArrayList;
import net.sf.jsqlparser.statement.Statement;


public class ExpressionTest extends TestCase {

    public ExpressionTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(ExpressionTest.class);
    }

    public void testDefaultValueIsFalse() {
        EgExpression expression = new EgExpression(null, "col1 = 0");
        assertEquals(false, expression.getValue());
    }

    public void testDefaultEvaluate() {
        EgExpression expression = new EgExpression(null, "col1 = 0");
        expression.setValue(false);
        assertEquals(false, expression.evaluate());
        expression.setValue(true);
        assertEquals(true, expression.evaluate());
    }

}
