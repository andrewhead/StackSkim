package com.headstrong.app;


public class EgCell {

    private Object mData;
    private boolean mSatisfiesExpressions;

    public EgCell(Object data, boolean satisfiesExpressions) {
        mData = data;
        mSatisfiesExpressions = satisfiesExpressions;
    }

    public Object getData() {
        return mData;
    }

    public boolean getSatisfiesExpressions() {
        return mSatisfiesExpressions;
    }

}
