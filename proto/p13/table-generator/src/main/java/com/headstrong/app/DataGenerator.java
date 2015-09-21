package com.headstrong.app;

import net.sf.jsqlparser.expression.Expression;
import net.sf.jsqlparser.expression.ExpressionVisitorAdapter;
import net.sf.jsqlparser.expression.BinaryExpression;
import net.sf.jsqlparser.expression.StringValue;
import net.sf.jsqlparser.expression.LongValue;
import net.sf.jsqlparser.expression.operators.relational.EqualsTo;
import net.sf.jsqlparser.expression.operators.relational.GreaterThan;
import net.sf.jsqlparser.expression.operators.relational.MinorThan;


public class DataGenerator extends ExpressionVisitorAdapter implements EgExpressionVisitor {

    private DataExtractor mExtractor = new DataExtractor();
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

    public Object generateData(Expression expr) {
        return generateData(expr, mSatisfy);
    }

    public Object generateData(Expression expr, boolean satisfy) {
        if (!(expr instanceof BinaryExpression)) {
            return null;
        }
        BinaryExpression binExpr = (BinaryExpression) expr;
        DataPosition pos = mExtractor.getDataPosition(binExpr);
        Object data = mExtractor.extractData(binExpr);
        if (pos == DataPosition.NONE) {
            return null;
        } else if (data != null) {
            return generateValue(binExpr.getStringExpression(), pos, data, satisfy);
        } else {
            return null;
        }
    }

    /**
     * Given a relational operation and a piece of data, generate an example of
     * data that violates the expression.
     */
    private Object generateValue(String opString, DataPosition pos, Object data, boolean satisfy) {
        if (opString.equals("=")) {
            if (satisfy == true) {
                return data;
            } else {
                if (data instanceof String) {
                    return "not " + data;
                }
                if (data instanceof Long) {
                    return ((Long) data).longValue() + 1;
                }
            }
        } else if (opString.equals(">") && pos == DataPosition.RIGHT) {
            return generateGreaterThan(data, satisfy);
        } else if (opString.equals("<") && pos == DataPosition.LEFT) {
            return generateGreaterThan(data, satisfy);
        }
        return data;
    }

    private Object generateGreaterThan(Object data, boolean satisfy) {
        if (data instanceof Long) {
            if (satisfy) {
                return ((Long) data).longValue() + 1;
            } else {
                return ((Long) data);
            }
        }
        return data;
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

    public Object getData() {
        return mData;
    }

}
