package com.headstrong.app;

import java.util.ArrayList;
import java.util.HashMap;

import net.sf.jsqlparser.JSQLParserException;
import net.sf.jsqlparser.parser.CCJSqlParserUtil;
import net.sf.jsqlparser.statement.select.Select;
import net.sf.jsqlparser.statement.select.SelectVisitor;
import net.sf.jsqlparser.statement.select.PlainSelect;
import net.sf.jsqlparser.statement.select.WithItem;
import net.sf.jsqlparser.statement.select.SetOperationList;
import net.sf.jsqlparser.statement.select.SelectItem;
import net.sf.jsqlparser.expression.ExpressionVisitor;
import net.sf.jsqlparser.statement.Statement;
import net.sf.jsqlparser.statement.StatementVisitorAdapter;

import net.sf.jsqlparser.expression.NullValue;
import net.sf.jsqlparser.expression.Function;
import net.sf.jsqlparser.expression.SignedExpression;
import net.sf.jsqlparser.expression.JdbcParameter;
import net.sf.jsqlparser.expression.JdbcNamedParameter;
import net.sf.jsqlparser.expression.DoubleValue;
import net.sf.jsqlparser.expression.LongValue;
import net.sf.jsqlparser.expression.DateValue;
import net.sf.jsqlparser.expression.TimeValue;
import net.sf.jsqlparser.expression.TimestampValue;
import net.sf.jsqlparser.expression.Parenthesis;
import net.sf.jsqlparser.expression.StringValue;
import net.sf.jsqlparser.expression.CaseExpression;
import net.sf.jsqlparser.expression.WhenClause;
import net.sf.jsqlparser.expression.AllComparisonExpression;
import net.sf.jsqlparser.expression.AnyComparisonExpression;
import net.sf.jsqlparser.expression.CastExpression;
import net.sf.jsqlparser.expression.AnalyticExpression;
import net.sf.jsqlparser.expression.WithinGroupExpression;
import net.sf.jsqlparser.expression.ExtractExpression;
import net.sf.jsqlparser.expression.IntervalExpression;
import net.sf.jsqlparser.expression.OracleHierarchicalExpression;
import net.sf.jsqlparser.expression.JsonExpression;
import net.sf.jsqlparser.expression.UserVariable;
import net.sf.jsqlparser.expression.NumericBind;
import net.sf.jsqlparser.expression.KeepExpression;
import net.sf.jsqlparser.expression.operators.arithmetic.Addition;
import net.sf.jsqlparser.expression.operators.arithmetic.BitwiseAnd;
import net.sf.jsqlparser.expression.operators.arithmetic.BitwiseOr;
import net.sf.jsqlparser.expression.operators.arithmetic.BitwiseXor;
import net.sf.jsqlparser.expression.operators.arithmetic.Concat;
import net.sf.jsqlparser.expression.operators.arithmetic.Division;
import net.sf.jsqlparser.expression.operators.arithmetic.Modulo;
import net.sf.jsqlparser.expression.operators.arithmetic.Multiplication;
import net.sf.jsqlparser.expression.operators.arithmetic.Subtraction;
import net.sf.jsqlparser.expression.operators.conditional.AndExpression;
import net.sf.jsqlparser.expression.operators.conditional.OrExpression;
import net.sf.jsqlparser.expression.operators.relational.Between;
import net.sf.jsqlparser.expression.operators.relational.EqualsTo;
import net.sf.jsqlparser.expression.operators.relational.ExistsExpression;
import net.sf.jsqlparser.expression.operators.relational.GreaterThan;
import net.sf.jsqlparser.expression.operators.relational.GreaterThanEquals;
import net.sf.jsqlparser.expression.operators.relational.InExpression;
import net.sf.jsqlparser.expression.operators.relational.IsNullExpression;
import net.sf.jsqlparser.expression.operators.relational.LikeExpression;
import net.sf.jsqlparser.expression.operators.relational.Matches;
import net.sf.jsqlparser.expression.operators.relational.MinorThan;
import net.sf.jsqlparser.expression.operators.relational.MinorThanEquals;
import net.sf.jsqlparser.expression.operators.relational.NotEqualsTo;
import net.sf.jsqlparser.expression.operators.relational.RegExpMatchOperator;
import net.sf.jsqlparser.expression.operators.relational.RegExpMySQLOperator;
import net.sf.jsqlparser.schema.Column;
import net.sf.jsqlparser.statement.select.SubSelect;


public class SelectExpressionExtractor extends StatementVisitorAdapter
    implements SelectVisitor, ExpressionVisitor {

    private Expression mRoot;
    private ArrayList<Expression> mLeafExpressions;
    private HashMap<net.sf.jsqlparser.expression.Expression, Expression> mExpressions = 
        new HashMap<net.sf.jsqlparser.expression.Expression, Expression>();

    public Expression visit(Statement statement) {
        mRoot = null;
        mLeafExpressions = new ArrayList<Expression>();
        statement.accept(this);
        return mRoot;
    }

    private Expression visitLeafExpression(net.sf.jsqlparser.expression.Expression sqlParserExpression) {
        return visitExpression(sqlParserExpression, true);
    }

    private Expression visitExpression(net.sf.jsqlparser.expression.Expression sqlParserExpression, boolean isLeaf) {
        Expression exp = new Expression(sqlParserExpression.toString());
        mExpressions.put(sqlParserExpression, exp);
        if (isLeaf == true) {
            mLeafExpressions.add(exp);
        }
        // If this is the first time visiting a condition, then save it as the tree root.
        if (mRoot == null) {
            mRoot = exp;
        }
        return exp;
    }

    public ArrayList<Expression> getLeafExpressions() {
        return mLeafExpressions;
    }

    @Override
    public void visit(AndExpression andExpression) {
        Expression exp = visitExpression(andExpression, false);
        net.sf.jsqlparser.expression.Expression left = andExpression.getLeftExpression();
        net.sf.jsqlparser.expression.Expression right = andExpression.getRightExpression();
        left.accept(this);
        right.accept(this);
        ArrayList<Expression> andChildren = exp.getChildren();
        andChildren.add(mExpressions.get(left));
        andChildren.add(mExpressions.get(right));
    }

    @Override
    public void visit(NullValue nullValue) {
        Expression exp = visitLeafExpression(nullValue);
    }

    @Override
    public void visit(Function function) {
        Expression exp = visitLeafExpression(function);
    }

    @Override
    public void visit(SignedExpression signedExpression) {
        Expression exp = visitLeafExpression(signedExpression);
    }

    @Override
    public void visit(JdbcParameter jdbcParameter) {
        Expression exp = visitLeafExpression(jdbcParameter);
    }

    @Override
    public void visit(JdbcNamedParameter jdbcNamedParameter) {
        Expression exp = visitLeafExpression(jdbcNamedParameter);
    }

    @Override
    public void visit(DoubleValue doubleValue) {
        Expression exp = visitLeafExpression(doubleValue);
    }
    
    @Override
    public void visit(LongValue longValue) {
        Expression exp = visitLeafExpression(longValue);
    }
    
    @Override
    public void visit(DateValue dateValue) {
        Expression exp = visitLeafExpression(dateValue);
    }

    @Override
    public void visit(TimeValue timeValue) {
        Expression exp = visitLeafExpression(timeValue);
    }

    @Override
    public void visit(TimestampValue timestampValue) {
        Expression exp = visitLeafExpression(timestampValue);
    }

    @Override
    public void visit(Parenthesis parenthesis) {
        Expression exp = visitLeafExpression(parenthesis);
    }

    @Override
    public void visit(StringValue stringValue) {
        Expression exp = visitLeafExpression(stringValue);
    }

    @Override
    public void visit(Addition addition) {
        Expression exp = visitLeafExpression(addition);
    }

    @Override
    public void visit(Division division) {
        Expression exp = visitLeafExpression(division);
    }

    @Override
    public void visit(Multiplication multiplication) {
        Expression exp = visitLeafExpression(multiplication);
    }

    @Override
    public void visit(Subtraction subtraction) {
        Expression exp = visitLeafExpression(subtraction);
    }

    @Override
    public void visit(OrExpression orExpression) {
        Expression exp = visitLeafExpression(orExpression);
    }

    @Override
    public void visit(Between between) {
        Expression exp = visitLeafExpression(between);
    }

    @Override
    public void visit(EqualsTo equalsTo) {
        Expression exp = visitLeafExpression(equalsTo);
    }

    @Override
    public void visit(GreaterThan greaterThan) {
        Expression exp = visitLeafExpression(greaterThan);
    }

    @Override
    public void visit(GreaterThanEquals greaterThanEquals) {
        Expression exp = visitLeafExpression(greaterThanEquals);
    }

    @Override
    public void visit(InExpression inExpression) {
        Expression exp = visitLeafExpression(inExpression);
    }

    @Override
    public void visit(IsNullExpression isNullExpression) {
        Expression exp = visitLeafExpression(isNullExpression);
    }

    @Override
    public void visit(LikeExpression likeExpression) {
        Expression exp = visitLeafExpression(likeExpression);
    }

    @Override
    public void visit(MinorThan minorThan) {
        Expression exp = visitLeafExpression(minorThan);
    }

    @Override
    public void visit(MinorThanEquals minorThanEquals) {
        Expression exp = visitLeafExpression(minorThanEquals);
    }

    @Override
    public void visit(NotEqualsTo notEqualsTo) {
        Expression exp = visitLeafExpression(notEqualsTo);
    }

    @Override
    public void visit(Column tableColumn) {
        Expression exp = visitLeafExpression(tableColumn);
    }

    @Override
    public void visit(SubSelect subSelect) {
        Expression exp = visitLeafExpression(subSelect);
    }

    @Override
    public void visit(CaseExpression caseExpression) {
        Expression exp = visitLeafExpression(caseExpression);
    }

    @Override
    public void visit(WhenClause whenClause) {
        Expression exp = visitLeafExpression(whenClause);
    }

    @Override
    public void visit(ExistsExpression existsExpression) {
        Expression exp = visitLeafExpression(existsExpression);
    }

    @Override
    public void visit(AllComparisonExpression allComparisonExpression) {
        Expression exp = visitLeafExpression(allComparisonExpression);
    }

    @Override
    public void visit(AnyComparisonExpression anyComparisonExpression) {
        Expression exp = visitLeafExpression(anyComparisonExpression);
    }

    @Override
    public void visit(Concat concat) {
        Expression exp = visitLeafExpression(concat);
    }

    @Override
    public void visit(Matches matches) {
        Expression exp = visitLeafExpression(matches);
    }

    @Override
    public void visit(BitwiseAnd bitwiseAnd) {
        Expression exp = visitLeafExpression(bitwiseAnd);
    }

    @Override
    public void visit(BitwiseOr bitwiseOr) {
        Expression exp = visitLeafExpression(bitwiseOr);
    }

    @Override
    public void visit(BitwiseXor bitwiseXor) {
        Expression exp = visitLeafExpression(bitwiseXor);
    }
    
    @Override
    public void visit(CastExpression cast) {
        Expression exp = visitLeafExpression(cast);
    }

    @Override
    public void visit(Modulo modulo) {
        Expression exp = visitLeafExpression(modulo);
    }

    @Override
    public void visit(AnalyticExpression aexpr) {
        Expression exp = visitLeafExpression(aexpr);
    }
    
    @Override
    public void visit(WithinGroupExpression wgexpr) {
        Expression exp = visitLeafExpression(wgexpr);
    }

    @Override
    public void visit(ExtractExpression eexpr) {
        Expression exp = visitLeafExpression(eexpr);
    }

    @Override
    public void visit(IntervalExpression iexpr) {
        Expression exp = visitLeafExpression(iexpr);
    }

    @Override
    public void visit(OracleHierarchicalExpression oexpr) {
        Expression exp = visitLeafExpression(oexpr);
    }

    @Override
    public void visit(RegExpMatchOperator rexpr) {
        Expression exp = visitLeafExpression(rexpr);
    }
    
    @Override
    public void visit(JsonExpression jsonExpr) {
        Expression exp = visitLeafExpression(jsonExpr);
    }

    @Override
    public void visit(RegExpMySQLOperator regExpMySQLOperator) {
        Expression exp = visitLeafExpression(regExpMySQLOperator);
    }
   
    @Override
    public void visit(UserVariable var) {
        Expression exp = visitLeafExpression(var);
    }
    
    @Override
    public void visit(NumericBind bind) {
        Expression exp = visitLeafExpression(bind);
    }
    
    @Override
    public void visit(KeepExpression aexpr) {
        Expression exp = visitLeafExpression(aexpr);
    }
    
    @Override
    public void visit(PlainSelect plainSelect) {
        plainSelect.getWhere().accept(this);
    }

    @Override
    public void visit(Select select) {
        select.getSelectBody().accept(this);
    }

    @Override
    public void visit(SetOperationList setOpList) {}

    @Override
    public void visit(WithItem withItem) {}

}
