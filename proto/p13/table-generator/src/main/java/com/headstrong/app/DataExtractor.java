package com.headstrong.app;

import net.sf.jsqlparser.schema.Column;
import net.sf.jsqlparser.expression.Expression;
import net.sf.jsqlparser.expression.BinaryExpression;
import net.sf.jsqlparser.expression.StringValue;
import net.sf.jsqlparser.expression.LongValue;


public class DataExtractor {

    public Object extractData(Expression expr) {
        if (expr instanceof BinaryExpression) {
            BinaryExpression binExpr = (BinaryExpression) expr;
            DataPosition pos = getDataPosition(binExpr);
            if (pos == DataPosition.LEFT) {
                return extractData(binExpr.getLeftExpression());
            } else if (pos == DataPosition.RIGHT) {
                return extractData(binExpr.getRightExpression());
            } else {
                return null;
            }
        } else if (expr instanceof StringValue) {
            return ((StringValue)expr).getValue();
        } else if (expr instanceof LongValue) {
            return ((LongValue)expr).getValue();
        }
        return null;
    }

    public DataPosition getDataPosition(BinaryExpression expr) {
        Expression left = expr.getLeftExpression();
        Expression right = expr.getRightExpression();
        if (left instanceof Column && isValue(right)) {
            return DataPosition.RIGHT;
        } else if (isValue(left) && right instanceof Column) {
            return DataPosition.LEFT;
        } else {
            return DataPosition.NONE;
        }
    }

    private boolean isValue(Expression expr) {
        return (
            expr instanceof StringValue ||
            expr instanceof LongValue
        );
    }

    private boolean hasColumnComparison(BinaryExpression expr) {
        Expression left = expr.getLeftExpression();
        Expression right = expr.getRightExpression();
        Object leftValue = extractData(left);
        Object rightValue = extractData(right);
        return (left instanceof Column && rightValue != null) ||
            (left != null && right instanceof Column);
    }

}

