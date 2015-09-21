package com.headstrong.app;

import java.util.List;
import java.util.HashSet;
import java.util.ArrayList;
import net.sf.jsqlparser.schema.Column;
import net.sf.jsqlparser.expression.Expression;
import net.sf.jsqlparser.expression.BinaryExpression;
import net.sf.jsqlparser.expression.LongValue;
import net.sf.jsqlparser.expression.StringValue;


public class ColumnTypeFinder {

    private DataExtractor mExtractor = new DataExtractor();

    public ColumnType getType(String columnName, List<EgExpression> exprs) {
        HashSet<ColumnType> foundTypes = new HashSet<ColumnType>();
        for (EgExpression expr: exprs) {
            ColumnType colType = getType(columnName, expr.getJsqlParserExpression());
            if (colType != null) {
                foundTypes.add(colType);
            }
        }
        if (foundTypes.size() > 1 || foundTypes.size() == 0) {
            return null;
        } else {
            ArrayList<ColumnType> typeList = new ArrayList<ColumnType>();
            typeList.addAll(foundTypes);
            return typeList.get(0);
        }
    }

    public ColumnType getType(String columnName, Expression expr) {
        if (expr instanceof BinaryExpression) {
            BinaryExpression binExpr = (BinaryExpression) expr;
            DataPosition pos = mExtractor.getDataPosition(binExpr);
            
            Expression dataExpression = null;
            String exprColumnName = null;
            if (pos == DataPosition.LEFT) {
                dataExpression = binExpr.getLeftExpression();
                Column column = (Column)binExpr.getRightExpression();
                exprColumnName = column.getColumnName();
            } else if (pos == DataPosition.RIGHT) {
                dataExpression = binExpr.getRightExpression();
                Column column = (Column)binExpr.getLeftExpression();
                exprColumnName = column.getColumnName();
            } else {
                return null;
            }

            if (!columnName.equals(exprColumnName)) {
                return null;
            }

            if (dataExpression instanceof LongValue) {
                return ColumnType.LONG;
            } else if (dataExpression instanceof StringValue) {
                return ColumnType.STRING;
            } else {
                return null;
            }
        } else {
            return null;
        }
    }

}

