package com.headstrong.app;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.util.Arrays;
import java.util.ArrayList;
import net.sf.jsqlparser.statement.Statement;


public class TruthTableTest extends TestCase {

    public TruthTableTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(TruthTableTest.class);
    }

    public void testEvaluations() {
        Statement stmt = TestJsqlParser.parse("SELECT col1 FROM tbl WHERE col1 = 0 AND col2 = 0");
        SelectExpressionExtractor selExtractor = new SelectExpressionExtractor();
        Expression root = selExtractor.visit(stmt);
        ArrayList<Expression> leafExpressions = selExtractor.getLeafExpressions();
        TruthTable truthTable = new TruthTable(root, leafExpressions);
        truthTable.evaluate();
        ArrayList<Evaluation> evaluations = truthTable.getEvaluations();
        assertEquals(4, evaluations.size());
        assertTrue(evaluations.contains(new Evaluation(true, true, true)));
        assertTrue(evaluations.contains(new Evaluation(false, true, false)));
        assertTrue(evaluations.contains(new Evaluation(false, false, true)));
        assertTrue(evaluations.contains(new Evaluation(false, false, false)));
    }

}
