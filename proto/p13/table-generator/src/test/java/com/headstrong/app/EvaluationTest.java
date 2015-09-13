package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.util.Arrays;
import java.util.ArrayList;
import net.sf.jsqlparser.statement.Statement;


public class EvaluationTest extends TestCase {

    public EvaluationTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(EvaluationTest.class);
    }

    public void testEvaluationsEqual() {
        Boolean[] values1 = {true, true, true, true};
        Boolean[] values2 = {true, true, true, true};
        ArrayList<Boolean> valuesList1 = new ArrayList<Boolean>(Arrays.asList(values1));
        ArrayList<Boolean> valuesList2 = new ArrayList<Boolean>(Arrays.asList(values2));
        Evaluation eval1 = new Evaluation(valuesList1, true);
        Evaluation eval2 = new Evaluation(valuesList2, true);
        assertEquals(eval1, eval2);
    }

    public void testEvaluationsUnequalIfValuesUnequal() {
        Boolean[] values1 = {true, true, true, true};
        Boolean[] values2 = {true, true, false, true};
        ArrayList<Boolean> valuesList1 = new ArrayList<Boolean>(Arrays.asList(values1));
        ArrayList<Boolean> valuesList2 = new ArrayList<Boolean>(Arrays.asList(values2));
        Evaluation eval1 = new Evaluation(valuesList1, true);
        Evaluation eval2 = new Evaluation(valuesList2, true);
        assertFalse(eval1.equals(eval2));
    }

    public void testEvaluationsUnequalIfResultsUnequal() {
        Boolean[] values1 = {true, true, true, true};
        Boolean[] values2 = {true, true, true, true};
        ArrayList<Boolean> valuesList1 = new ArrayList<Boolean>(Arrays.asList(values1));
        ArrayList<Boolean> valuesList2 = new ArrayList<Boolean>(Arrays.asList(values2));
        Evaluation eval1 = new Evaluation(valuesList1, true);
        Evaluation eval2 = new Evaluation(valuesList2, false);
        assertFalse(eval1.equals(eval2));
    }

}
