package com.headstrong.app;

import net.sf.jsqlparser.expression.Expression;
import java.util.ArrayList;

/**
 * Expression from a SQL WHERE clause
 */
public class EgExpression {

    private Expression mJsqlParserExpression;
    private String mText;
    private ArrayList<EgExpression> mChildren = new ArrayList<EgExpression>();
    private boolean mValue = false;

    public EgExpression(Expression jsqlParserExpression, String text) {
        mJsqlParserExpression = jsqlParserExpression;
        mText = text;
    }

    public void setValue(boolean value) {
        mValue = value;
    }

    public boolean getValue() {
        return mValue;
    }

    public ArrayList<EgExpression> getChildren() {
        return mChildren;
    }

    public boolean evaluate() {
        return mValue;
    }
    
    public Expression getJsqlParserExpression() {
        return mJsqlParserExpression;
    }

    public void accept(EgExpressionVisitor expVisitor) {
        expVisitor.visit(this);
    }

    public String toString() {
        return mText;
    }

}
