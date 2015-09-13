package com.headstrong.app;

import java.util.ArrayList;
import java.util.Arrays;


/**
 * Takes compound SQL expression and its constiuent expressions to generate 
 * when the expression is satisfied
 */
public class TruthTable {

    private Expression mRoot;
    private ArrayList<Expression> mVariables;
    private ArrayList<Evaluation> mEvaluations;

    public TruthTable(Expression rootExpression, ArrayList<Expression> variables) {
        mRoot = rootExpression;
        mVariables = variables;
    }

    @SuppressWarnings("unchecked")
    public void evaluate() {

        ArrayList<ArrayList<Boolean>> valueCombos = new ArrayList<ArrayList<Boolean>>();

        // Generate all possible combinations of variable values
        for (int i = 0; i < mVariables.size(); i++) {
            if (i == 0) {
                valueCombos = new ArrayList<ArrayList<Boolean>>();
                valueCombos.add(new ArrayList<Boolean>(Arrays.asList(true)));
                valueCombos.add(new ArrayList<Boolean>(Arrays.asList(false)));
            } else {
                ArrayList<ArrayList<Boolean>> newValueCombos = new ArrayList<ArrayList<Boolean>>();
                for (ArrayList<Boolean> combo: valueCombos) {
                    ArrayList<Boolean> newCombo0 = (ArrayList<Boolean>)combo.clone();
                    ArrayList<Boolean> newCombo1 = (ArrayList<Boolean>)combo.clone();
                    newCombo0.add(0, true);
                    newCombo1.add(0, false);
                    newValueCombos.add(newCombo0);
                    newValueCombos.add(newCombo1);
                }
                valueCombos = newValueCombos;
            }
        }

        // Compute the evaluations for every combination of input
        mEvaluations = new ArrayList<Evaluation>();
        for (ArrayList<Boolean> combo: valueCombos) {
            for (int i = 0; i < mVariables.size(); i++) {
                Expression leafExpression = mVariables.get(i);
                leafExpression.setValue(combo.get(i));
            }
            boolean result = mRoot.evaluate();
            mEvaluations.add(new Evaluation(combo, result));
        }
    }

    public ArrayList<Evaluation> getEvaluations() {
        return mEvaluations;
    }

}
