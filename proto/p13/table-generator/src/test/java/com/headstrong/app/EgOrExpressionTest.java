package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import static org.junit.Assert.*;


public class EgOrExpressionTest extends TestCase {

    public EgOrExpressionTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(EgOrExpressionTest.class);
    }

    public void testEvaluateOr() {
        EgExpression left = new EgExpression(null, "col1 = 0");
        EgExpression right = new EgExpression(null, "col2 = 0");
        EgOrExpression exp = new EgOrExpression(null, "col1 = 0 AND col2 = 0");
        exp.getChildren().add(left);
        exp.getChildren().add(right);
        left.setValue(false); right.setValue(false);
        assertEquals(false, exp.evaluate());
        left.setValue(true); right.setValue(false);
        assertEquals(true, exp.evaluate());
        left.setValue(false); right.setValue(true);
        assertEquals(true, exp.evaluate());
        left.setValue(true); right.setValue(true);
        assertEquals(true, exp.evaluate());
    }

}
