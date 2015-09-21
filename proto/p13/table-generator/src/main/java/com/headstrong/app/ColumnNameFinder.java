package com.headstrong.app;

import net.sf.jsqlparser.schema.Column;
import net.sf.jsqlparser.expression.Expression;
import net.sf.jsqlparser.expression.BinaryExpression;


public class ColumnNameFinder {

    private DataExtractor mExtractor = new DataExtractor();

    public String getName(Expression expr) {
        if (expr instanceof BinaryExpression) {
            BinaryExpression binExpr = (BinaryExpression) expr;
            return getName(binExpr);
        }
        return null;   
    }

    public String getName(BinaryExpression expr) {
        DataPosition pos = mExtractor.getDataPosition(expr);
        if (pos == DataPosition.LEFT) {
            Column col = (Column) expr.getRightExpression();
            return col.getColumnName();
        } else if (pos == DataPosition.RIGHT) {
            Column col = (Column) expr.getLeftExpression();
            return col.getColumnName();
        } else {
            return null;
        }
    }

}
