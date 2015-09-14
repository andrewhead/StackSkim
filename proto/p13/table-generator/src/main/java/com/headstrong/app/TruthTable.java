package com.headstrong.app;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.BitSet;
import java.util.HashMap;
import java.util.HashSet;


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

    public ArrayList<Evaluation> getTrueEvaluations() {
        ArrayList<Evaluation> trueEvaluations = new ArrayList<Evaluation>();
        for (Evaluation eval: mEvaluations) {
            if (eval.getResult() == true) {
                trueEvaluations.add(eval);
            }
        }
        return trueEvaluations;
    }

    /**
     * Get list of evaluations that fail due to one bit being flipped from
     * a truth evaluation.
     */
    public ArrayList<Evaluation> getOneOffEvaluations() {
        HashSet<Evaluation> oneOffEvaluationSet = new HashSet<Evaluation>();
        for (int i = 0; i < mVariables.size(); i++) {
            oneOffEvaluationSet.addAll(getOneOffEvaluations(i));
        }
        ArrayList<Evaluation> oneOffEvaluationList = new ArrayList<Evaluation>();
        oneOffEvaluationList.addAll(oneOffEvaluationSet);
        return oneOffEvaluationList;
    }

    public ArrayList<Evaluation> getOneOffEvaluations(int varIndex) {

        HashSet<Evaluation> oneOffEvaluations = new HashSet<Evaluation>();

        // Index evaluations by their bits
        HashMap<BitSet,Evaluation> bitsets = new HashMap<BitSet,Evaluation>();
        for (Evaluation eval: mEvaluations) {
            ArrayList<Boolean> values = eval.getValues();
            BitSet bitset = new BitSet(values.size());
            for (int i = 0; i < values.size(); i++) {
                bitset.set(i, values.get(i));
            }
            bitsets.put(bitset, eval);
        }

        // Find all rows in the table with 'false' output based on one bit
        // changing from a configuration with a 'true' output 
        for (Evaluation eval: mEvaluations) {
            if (eval.getResult() == true) {
                ArrayList<Boolean> values = eval.getValues();
                BitSet oneOffKey = new BitSet(values.size());
                for (int j = 0; j < values.size(); j++) {
                    oneOffKey.set(j, values.get(j));
                }
                oneOffKey.flip(varIndex);
                Evaluation oneOffEvaluation = bitsets.get(oneOffKey);
                if (oneOffEvaluation.getResult() == false) {
                    oneOffEvaluations.add(oneOffEvaluation);
                }
            }
        }        
    
        ArrayList<Evaluation> oneOffEvaluationList = new ArrayList<Evaluation>();
        oneOffEvaluationList.addAll(oneOffEvaluations);
        return oneOffEvaluationList;

    }

}
