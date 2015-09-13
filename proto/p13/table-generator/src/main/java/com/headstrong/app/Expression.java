package com.headstrong.app;

import java.util.ArrayList;

/**
 * Expression from a SQL WHERE clause
 */
public class Expression {

    private String mText;
    private ArrayList<Expression> mChildren = new ArrayList<Expression>();
    private boolean mValue = false;

    public Expression(String text) {
        mText = text;
    }

    public void setValue(boolean value) {
        mValue = value;
    }

    public boolean getValue() {
        return mValue;
    }

    public ArrayList<Expression> getChildren() {
        return mChildren;
    }

    public String toString() {
        return mText;
    }

    public boolean evaluate() {
        return mValue;
    }

}
