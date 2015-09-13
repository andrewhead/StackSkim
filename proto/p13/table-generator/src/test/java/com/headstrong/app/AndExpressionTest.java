package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;


public class AndExpressionTest extends TestCase {

    public AndExpressionTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(AndExpressionTest.class);
    }

    public void testEvaluateAnd() {
        Expression left = new Expression("col1 = 0");
        Expression right = new Expression("col2 = 0");
        AndExpression exp = new AndExpression("col1 = 0 AND col2 = 0");
        exp.getChildren().add(left);
        exp.getChildren().add(right);
        left.setValue(false); right.setValue(false);
        assertEquals(false, exp.evaluate());
        left.setValue(true); right.setValue(false);
        assertEquals(false, exp.evaluate());
        left.setValue(false); right.setValue(true);
        assertEquals(false, exp.evaluate());
        left.setValue(true); right.setValue(true);
        assertEquals(true, exp.evaluate());
    }

}
