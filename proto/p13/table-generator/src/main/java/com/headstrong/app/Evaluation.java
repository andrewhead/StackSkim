package com.headstrong.app;

import java.util.ArrayList;


public class Evaluation {
    
    private ArrayList<Boolean> mValues;
    private boolean mResult;

    public Evaluation(ArrayList<Boolean> values, boolean result) {
        mValues = values;
        mResult = result;
    }

    public Evaluation(boolean result, boolean... values) {
        ArrayList<Boolean> valuesList = new ArrayList<Boolean>();
        for (boolean v: values) {
            valuesList.add(v);
        }
        mValues = valuesList;
        mResult = result;
    }

    public ArrayList<Boolean> getValues() {
        return mValues;
    }

    public boolean getResult() {
        return mResult;
    }

    @Override
    public int hashCode() {
        int code = mValues.size();
        for (boolean value : mValues) {
            code = code * 2;
            if (value) {
                code = code + 1;
            }
        }
        code = code * 2;
        if (mResult) {
            code = code + 1;
        }
        return 0;
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Evaluation)) {
            return false;
        }
        Evaluation otherEval = (Evaluation) o;
        return (this.mValues.equals(otherEval.mValues)) &&
            (this.mResult == otherEval.mResult);
    }

    public String toString() {
        return "Result: " + mResult + ", Output: " + mValues.toString();
    }

}
