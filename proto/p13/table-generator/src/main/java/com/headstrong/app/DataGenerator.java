package com.headstrong.app;

import net.sf.jsqlparser.expression.Expression;
import net.sf.jsqlparser.expression.ExpressionVisitorAdapter;
import net.sf.jsqlparser.expression.BinaryExpression;
import net.sf.jsqlparser.expression.StringValue;
import net.sf.jsqlparser.expression.LongValue;
import net.sf.jsqlparser.expression.operators.relational.EqualsTo;
import net.sf.jsqlparser.expression.operators.relational.GreaterThan;
import net.sf.jsqlparser.expression.operators.relational.MinorThan;
import net.sf.jsqlparser.schema.Column;


public class DataGenerator extends ExpressionVisitorAdapter implements EgExpressionVisitor {

    private Object mData;
    private boolean mSatisfy;

    /**
     * @param satisfy whether data generated should satisfy the expressions or violate them
     */
    public DataGenerator(boolean satisfy) {
        mSatisfy = satisfy;
    }

    public DataGenerator() {
        this(true);
    }

    @Override
    public void visit(EgExpression exp) {
        mData = null;
        exp.getJsqlParserExpression().accept(this);
    }

    private Object generateData(BinaryExpression expr) {
        if (!hasColumnComparison(expr)) return null;
        Expression left = expr.getLeftExpression();
        Expression right = expr.getRightExpression();
        Object leftValue = getValue(left);
        Object rightValue = getValue(right);
        if (left instanceof Column && rightValue != null) {
            return generateValue(expr.getStringExpression(), true, rightValue);
        } else if (left != null && right instanceof Column) {
            return generateValue(expr.getStringExpression(), false, leftValue);
        }
        return null;
    }

    /**
     * Given a relational operation and a piece of data, generate an example of
     * data that violates the expression.
     */
    private Object generateValue(String opString, boolean dataOnRight, Object data) {
        if (opString.equals("=")) {
            if (mSatisfy == true) {
                return data;
            } else {
                if (data instanceof Long) {
                    return ((Long) data).longValue() + 1;
                }
            }
        } else if (opString.equals(">") && dataOnRight) {
            return generateGreaterThan(data);
        } else if (opString.equals("<") && !dataOnRight) {
            return generateGreaterThan(data);
        }
        return data;
    }

    private Object generateGreaterThan(Object data) {
        if (data instanceof Long) {
            return ((Long) data).longValue() + 1;
        }
        return data;
    }

    private boolean hasColumnComparison(BinaryExpression expr) {
        Expression left = expr.getLeftExpression();
        Expression right = expr.getRightExpression();
        Object leftValue = getValue(left);
        Object rightValue = getValue(right);
        return (left instanceof Column && rightValue != null) ||
            (left != null && right instanceof Column);
    }

    @Override
    public void visit(EqualsTo equalsTo) {
        mData = generateData(equalsTo);
    }

    @Override
    public void visit(GreaterThan greaterThan) {
        mData = generateData(greaterThan);
    }

    @Override
    public void visit(MinorThan minorThan) {
        mData = generateData(minorThan);
    }

    private Object getValue(Expression exp) {
        if (exp instanceof StringValue) {
            return ((StringValue)exp).getValue();
        } else if (exp instanceof LongValue) {
            return ((LongValue)exp).getValue();
        }
        return null;
    }

    public Object getData() {
        return mData;
    }

}
